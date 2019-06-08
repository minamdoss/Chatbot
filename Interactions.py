from DBConnection import Database as DB


#cursor = DB().CursorConnection()

class intent :

     def GetIntent(self , Name):
            conn , cursor = DB().DBconnect()
            command = """
            Select ID From CBT_LKP_Intent Where Name = '{0}'
            """.format(Name)
            try:
                tpl = []
                cursor.execute(command)
                for row in cursor:
                    tpl.append(row)
            except Exception as e:
                print("Error ", e)
            DB().DBdisconnect()
            return tpl

     def SaveIntent ( self, name ):
        conn , cursor = DB().DBconnect()
        command ="""
        EXEC CBT_LKP_Intent_INS @Name=?
        """
        arg = name
        try:
            cursor.execute(command,arg)
            print("Inserted Successfully")
            conn.commit()
        except Exception as e:
            print("Error ",e)
        DB().DBdisconnect()


     def UpdateIntent(self,id,name):
        conn , cursor = DB().DBconnect()
        command ="""
        EXEC CBT_LKP_Intent_UPD @ID=? ,@Name=? 
        """
        arg = (id,name)
        try:
            cursor.execute(command,arg)
            print("Updated Successfully")
            conn.commit()

        except Exception as e:
            print("Error ",e)
        DB().DBdisconnect()

     def DeleteIntent(self,id):
        conn , cursor = DB().DBconnect()
        command ="""
        EXEC CBT_LKP_Intent_DEL @ID=?
        """
        arg = id
        try:
            cursor.execute(command,arg)
            print("Deleted Successfully")
            conn.commit()

        except Exception as e:
            print("Error ",e)
        DB().DBdisconnect()

class slots:

    def GetIntentSlot(self , IntentName):
        conn , cursor = DB().DBconnect()
        command = """
        Select Slot From CBT_LNK_IntentSlot_VIW Where Intent = '{0}'   
        """.format(IntentName)
        try:
            tpl =[]
            cursor.execute(command)
            for row in cursor:
                tpl.append(row)
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()
        return tpl

    def ShowSlots(self):
        conn , cursor = DB().DBconnect()
        command = """
        Select * From CBT_LKP_Slot
        """
        try:
            cursor.execute(command)
            for row in cursor:
                print(row)
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

    def GetSlot(self,name):
        conn , cursor = DB().DBconnect()
        command = """
        Select ID From CBT_LKP_Slot Where Name = '{0}'
        """.format(name)
        try:
            tpl = []
            cursor.execute(command)
            for row in cursor:
                tpl.append(row)
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()
        return tpl


    def SaveSlot(self,name):
        conn , cursor = DB().DBconnect()
        command ="""
        EXEC CBT_LKP_Slot_INS @Name=? 
        """
        arg =name
        try:
            cursor.execute(command,arg)
            print("Inserted Successfully")
            conn.commit()
        except Exception as e:
            print("Error ",e)
        DB().DBdisconnect()


    def SaveIntentSlot(self,intentID,slotID):
        conn , cursor = DB().DBconnect()
        command ="""
        EXEC CBT_LNK_IntentSlot_INS @IntentID=? , @SlotID=?
        """
        arg =(intentID,slotID)
        try:
            cursor.execute(command,arg)
            print("Inserted Successfully")
            conn.commit()
        except Exception as e:
            print("Error ",e)
        DB().DBdisconnect()


    def UpdateSlot(self,id,name):
        conn , cursor = DB().DBconnect()
        command ="""
        EXEC CBT_LKP_Slot_UPD @ID=? ,@Name=? 
        """
        arg = (id,name)
        try:
            cursor.execute(command,arg)
            print("Updated Successfully")
            conn.commit()

        except Exception as e:
            print("Error ",e)
        DB().DBdisconnect()



    def UpdateIntentSlot(self,id,intent,slot):
        conn , cursor = DB().DBconnect()
        command ="""
        EXEC CBT_LNK_IntentSlot_UPD @ID=? ,@IntentID=? ,@SlotID=?
        """
        arg = (id,intent,slot)
        try:
            cursor.execute(command,arg)
            print("Updated Successfully")
            conn.commit()

        except Exception as e:
            print("Error ",e)
        DB().DBdisconnect()


    def DeleteSlot(self,id):
        conn , cursor = DB().DBconnect()
        command ="""
        EXEC CBT_LKP_Slot_DEL @ID=?
        """
        arg = id
        try:
            cursor.execute(command,arg)
            print("Deleted Successfully")
            conn.commit()

        except Exception as e:
            print("Error ",e)
        DB().DBdisconnect()

    def DeleteIntentSlot(self,id):
        conn , cursor = DB().DBconnect()
        command ="""
        EXEC CBT_LNK_IntentSlot_DEL @ID=?
        """
        arg = id
        try:
            cursor.execute(command,arg)
            print("Deleted Successfully")
            conn.commit()

        except Exception as e:
            print("Error ",e)
        DB().DBdisconnect()

class logs:

    def __logs_insert__(self ,Q , A ):
        conn , cursor = DB().DBconnect()
        command = """
                  EXEC CBT_Log_INS @Question=? , @Answer=?
                  """
        arg = ( Q , A )
        try:
            cursor.execute(command, arg)
            print("Inserted Successfully")
            conn.commit()

        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

    def __logs_update__(self, _id ,Q , A ):
        conn , cursor = DB().DBconnect()
        command = """
                          EXEC CBT_Log_UPD @ID=?, @Question=? , @Answer=?
                          """
        arg = (_id , Q , A )
        try:
            cursor.execute(command, arg)
            print("Updated Successfully")
            conn.commit()
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

    def __logs_delete__(self, _id):
        conn , cursor = DB().DBconnect()
        command = """
                             EXEC CBT_Log_DEL @ID=?
                             """
        arg = _id
        try:
            cursor.execute(command, arg)
            print("Deleted Successfully")
            conn.commit()
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

class feedback:

    def __feedback_insert__(self , Log_ID, Rate, Message):
        conn , cursor = DB().DBconnect()
        command = """
               EXEC CBT_Feedback_INS @logid=? , @rate=? , @text=?
               """
        arg = (Log_ID, Rate, Message)
        try:
            cursor.execute(command, arg)
            print("Inserted Successfully")
            conn.commit()
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

    def __feedback_delete__(self, _id):
        conn , cursor = DB().DBconnect()
        command = """
               EXEC CBT_Feedback_DEL @id=?
               """
        arg = _id
        try:
            cursor.execute(command, arg)
            print("Deleted Successfully")
            conn.commit()
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

    def __feedback_update__(self, _id , Log_ID, Rate, Message):
        conn , cursor = DB().DBconnect()
        command = """
               EXEC CBT_Feedback_UPD @id=?, @logid=? , @rate=? , @text=?
               """
        arg = (_id, Log_ID, Rate, Message)
        try:
            cursor.execute(command, arg)
            print("updated Successfully")
            conn.commit()
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

class lowProb:

    def __lowProb_selectAll__(self):
        conn , cursor = DB().DBconnect()
        command = """
                          select Question , Intent from CBT_LowProb_VIW
                          """
        try:
            cursor.execute(command)
            for row in cursor:
                print(row)
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

    def __lowProb_selectIntent__(self, ID):
        conn , cursor = DB().DBconnect()
        command = """
                          select * from CBT_LowProb_VIW where IntentID= %d
                          """ % ID

        try:
            cursor.execute(command)
            for row in cursor:
                print(row)
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

    def __lowProb_insert__(self , Q, IntentID):
        conn , cursor = DB().DBconnect()
        command = """
                  EXEC CBT_LowProb_INS @Question=?, @IntentID=?
                  """
        arg = (Q, IntentID)
        try:
            cursor.execute(command, arg)
            print("Inserted Successfully")
            conn.commit()
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

    def __lowProb_update__(self, _id , Q, IntentID):
        conn , cursor = DB().DBconnect()
        command = """
                          EXEC CBT_LowProb_UPD @ID=?, @Question=?, @IntentID=?
                          """
        arg = (_id, Q, IntentID)
        try:
            cursor.execute(command, arg)
            print("Updated Successfully")
            conn.commit()
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

    def __lowProb_delete__(self, _id):
        conn , cursor = DB().DBconnect()
        command = """
                             EXEC CBT_LowProb_DEL @ID=?
                             """
        arg = _id
        try:
            cursor.execute(command, arg)
            print("Deleted Successfully")
            conn.commit()
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

class UnAnswered:

    def __noIntent_selectAll__(self):
        conn , cursor = DB().DBconnect()
        command = """
                          select Question from CBT_NoIntent_VIW
                          """
        try:
            cursor.execute(command)
            for row in cursor:
                print(row)
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

    def __noIntent_insert__( self , Q ):
        conn , cursor = DB().DBconnect()
        command = """
                  EXEC CBT_NoIntent_INS @Question=?
                  """
        arg = Q
        try:
            cursor.execute(command, arg)
            print("Inserted Successfully")
            conn.commit()
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

    def __noIntent_update__(self, _id , Q):
        conn , cursor = DB().DBconnect()
        command = """
                          EXEC CBT_NoIntent_UPD @ID=?, @Question=?
                          """
        arg = (_id, Q)
        try:
            cursor.execute(command, arg)
            print("Updated Successfully")
            conn.commit()
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()

    def __noIntent_delete__(self, _id):
        conn , cursor = DB().DBconnect()
        command = """
                             EXEC CBT_NoIntent_DEL @ID=?
                             """
        arg = _id
        try:
            cursor.execute(command, arg)
            print("Deleted Successfully")
            conn.commit()
        except Exception as e:
            print("Error ", e)
        DB().DBdisconnect()


