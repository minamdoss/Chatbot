from Interactions import lowProb , slots , feedback , logs , UnAnswered ,intent

class interaction():


    def LogFactory(self):
       return logs()


    def FeedbackFactory(self):
       return feedback()

    def LowProbFactory(self):
       return lowProb()

    def UnAnsweredFactory(self):
        return UnAnswered()

    def IntentFactory(self):
        return intent()

    def SlotFactory(self):
        return slots()


#interaction().SlotFactory().SaveSlot('CourseName')
#interaction().IntentFactory().SaveIntent('ReqCourseDescription')
#intent = interaction().IntentFactory().GetIntent('ReqCourseDescription')
#slot = interaction().SlotFactory().GetSlot('CourseName')
#interaction().SlotFactory().SaveIntentSlot(intent[0][0],slot[0][0])

#x = (interaction().SlotFactory().GetIntentSlot('ReqSchedule'))
#interaction().SlotFactory().DeleteIntentSlot(1005)
#print(x[0][0])
