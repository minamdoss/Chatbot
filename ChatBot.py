from past.builtins import raw_input
from NLU_Engine import NLU
from googletrans import Translator
#### Feedback
#### Logs
#### Another Question while asking for entity value
#### Change Yaml entities values to LowerCase
#### Response
def Translate_Text (question):
    translator = Translator()
    translated = translator.translate(question )
    print("Source Language : " + translated.src)
    print("Destination Language : " + translated.dest)
    print("Origin Text : " + translated.origin)
    print("Translated Text : " + translated.text)
    return translated.text , translated.src
    # print("Pronunciation : " + str(translated.pronunciation))

if __name__ == "__main__":

    flag = 1
    nlu = NLU()
    nlu.EngineMode("Train")
    while (flag):
        question = raw_input("User : ")

        #To End Chat
        if(question == 'q'):
            flag = 0
            break

        # print(eda(question))

        # nlu.setQuery(Translate_Text(question))
        nlu.setQuery((question))

        nlu.answer()




