import io
import json
import re
import pandas as pd
import snips_nlu_en
from snips_nlu import SnipsNLUEngine, load_resources
from snips_nlu.default_configs import CONFIG_EN
from googletrans import Translator
import app
from DBConnection import Database
from DB_Interaction import interaction

class NLU:
    __connection = Database()
    __interaction = interaction()
    __answers = {
            "NA": "Please Ask your department administrator for this"
        }
    def __Translate_Text (question,x='en'):
        translator = Translator()
        translated = translator.        translate(question , dest=x)
        print("Source Language : " + translated.src)
        print("Destination Language : " + translated.dest)
        print("Origin Text : " + translated.origin)
        print("Translated Text : " + translated.text)
        return translated.text

    def __int__(self):
        self._query = ''
        self.__result = ''
        self._intent = ''
        self._probability = 0
        self._slots = {}
        self.__engine=''
        self.__dataset=''
        self.__nluSlots=''
        self.language=''

    def EngineMode(self, mode):
        """
        Saving the engine to use the model for every question (Training Part)
        or Use the model if it already exists (Testing Part)

        :param mode: Test or Train string
        :return:  Fitted Engine
        """


        if mode =="Train":
            load_resources('snips_nlu_en')

            self.__engine = SnipsNLUEngine(config=CONFIG_EN)
            with io.open("dataset.json") as f:
               self.__dataset = json.load(f)

            self.__engine.fit(self.__dataset)

            #UnComment to save the model
            #self.__engine.persist("Z:\FCIS-ASU\Semester 8\ChatbotModel")

        elif mode =="Test":
            with io.open("dataset.json") as f:
               self.__dataset = json.load(f)
            self.__engine = SnipsNLUEngine.from_path("Z:\FCIS-ASU\Semester 8\ChatbotModel")



    def setQuery(self, query):
        # self._query , self.language = query
        self._query = query
        self.__excute()



    def __excute(self):
        parsing = self.__engine.parse(self._query)
        self.__result = json.loads(json.dumps(parsing,indent=1))
        print( self.__result )

    def _getIntent(self):
        try:
            self._intent = self.__result['intent']['intentName']
            return self._intent
        except Exception as e:
            return 'None'


    def _getProbability(self):
        self._probability = self.__result['intent']['probability']
        return self._probability

    #need Handling Exception
    def _getSlots(self):
        dic = {}
        if len(self.__result['slots']) != 0:
            for x in range(len(self.__result['slots'])):
                if not re.search("Val",self.__result['slots'][x]['entity']):
                    if str(self.__result['slots'][x]['entity']).__contains__("snips"):
                        dic[self.__result['slots'][x]['slotName']] = self.__result['slots'][x]['rawValue']
                    else:
                        if re.search(" ?",self.__result['slots'][x]['rawValue']):
                            self.__result['slots'][x]['rawValue'] =self.__result['slots'][x]['rawValue'].replace('?', '')
                            print(self.__result['slots'][x]['rawValue'])
                        dic[self.__result['slots'][x]['entity']] = self.__result['slots'][x]['rawValue']
        else:
            return "No Slots"

        self._slots = dic
        return self._slots


    def checkIntent(self):
        if self._getIntent() == 'None':
            self.__interaction.UnAnsweredFactory().__noIntent_insert__(self._query)
            return False
        else:
            return True


    def answer(self):
        """
             Check if the question has intent or None

        :return: Answer
        """
        

        if self.checkIntent():
            if str(self.CheckJsonEntities()).__contains__("Has No Entities"):
                print("Chatbot : Get Answer From Json Answers")
                # app.receive_message("Chatbot : Get Answer From Json Answers")
            else:
                self.return_original()
        else:
            print('ChatBot : not available due to intent')

    def checkSlots(self):
        self.__nluSlots = self._getSlots()
        if str(self.__nluSlots).__contains__("No Slots") :
            return "No"
        datasetSlots = []
        print(self._getIntent())
        for i in range(len(self.__dataset['intents'][self._getIntent()]['utterances'])):
            for j in range(len(self.__dataset['intents'][self._getIntent()]['utterances'][i]['data'])):
                check = json.dumps(self.__dataset['intents'][self._getIntent()]['utterances'][i]['data'][j])
                if 'entity' in check:
                    if str(self.__dataset['intents'][self._getIntent()]['utterances'][i]['data'][j]['entity']).__contains__("snips"):
                        datasetSlots.append(self.__dataset['intents'][self._getIntent()]['utterances'][i]['data'][j]['slot_name'])
                    else:
                        datasetSlots.append(self.__dataset['intents'][self._getIntent()]['utterances'][i]['data'][j]['entity'])
                    datasetSlots = list(dict.fromkeys(datasetSlots))
        for x in datasetSlots:
            if 'Val' in x:
                datasetSlots.remove(x)
        ret = []
        for i in range(len(datasetSlots)):
            found = False
            for j in self.__nluSlots.keys():
                if datasetSlots[i] == j:
                    found = True
                    break
            if not found:
                ret.append(datasetSlots[i])
        print("Slots Not Available in Question : ", ret)  # el mafroud btalla3 el slots ely el mafroud tb2a mwgooda
        return ret


    def askForunenteredEntities(self):
        slots_needed = self._getSlots()
        # print(slots_needed)
        slots_missing = self.checkSlots()
        if str(slots_missing).__contains__("No"):
            return
        loopflagi = True
        # print(temp3[1]);
        for i in range(len(slots_missing)):
            loopflagi = False
            while not loopflagi:

                chatbotques = "Please Enter "+slots_missing[i]
                # g = Translator().translate(chatbotques , dest = self.language).text
                # print("Chatbot: ",g)
                print ("Chatbot : ",chatbotques)
                if slots_missing[i] == "ID":
                    try:
                        reply = int(input("User: "))
                    except:
                        print("Chatbot: Please Enter a valid ID")
                        continue
                else:
                    reply = input("User: ")

                if reply == 'q':
                    break
                if str(slots_missing[i]).__contains__("ID"):
                    self.__nluSlots[slots_missing[i]] = reply
                    break
                for j in range(len(self.__dataset['entities'][slots_missing[i]])):
                    try:
                        check = json.dumps(self.__dataset['entities'][slots_missing[i]]['data'][j])
                    except:
                        continue
                    if reply in check:
                        # e3ml 7aga
                        self.__nluSlots[slots_missing[i]] = reply
                        loopflagi = True
                        break
        return self.__nluSlots

    def return_original(self):
        slots_needed = self.askForunenteredEntities()
        if slots_needed is None:
            self.__interaction.UnAnsweredFactory().__noIntent_insert__(self._query)
            print("ChatBot : I don't have answer for this")
            return

        key_list = list(slots_needed.keys())

        # print(key_list)
        finaldic = dict()
        for key in range(len(key_list)):
            # print(key_list[key] + "here")
            # print(slots_needed[key_list[key]])
            # do something
            if key_list[key] == "ID":
                continue
            # print("Key :",key_list[key])

            try:
                for i in range(len(self.__dataset['entities'][key_list[key]]["data"])):
                    check = json.dumps(self.__dataset['entities'][key_list[key]]["data"][i])
                    if slots_needed[key_list[key]] in check:
                        self.__nluSlots[key_list[key]] = self.__dataset['entities'][key_list[key]]["data"][i]["value"]
                        # print(self.__dataset['entities'][key_list[key]]["data"][i]["value"])
            except:
                print("Error")

        print("Values to get from Database" , self.__nluSlots)  # original values of entities used in question
        # return List or dictionary??



    def CheckJsonEntities(self):
         for i in range(len(self.__dataset['intents'][self._getIntent()]['utterances'])):
                for j in range(len(self.__dataset['intents'][self._getIntent()]['utterances'][i]['data'])):
                    check = json.dumps(self.__dataset['intents'][self._getIntent()]['utterances'][i]['data'][j])
                    print(check)
                    if 'entity' in check:
                        print("Entities")
                        return "Has Entities"
                    else:
                        print("No Entities")

                print("-----------")
         print("Exit with No Entities")
         return "Has No Entities"
