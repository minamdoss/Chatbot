import pyodbc as db



class Database:

    def __init__(self):
        self.dbconn = db.connect("Driver={SQL SERVER};Server=.;Database=CBT;Trusted_Connection=yes;")
        self.cursor = self.dbconn.cursor()

    def DBconnect(self):
        print("Connecting to Database...")
        return self.dbconn , self.cursor

    def CursorConnection(self):
        return self.cursor

    def DBdisconnect(self):
        print("Disconnecting from Database...")
        self.cursor.close()
        self.dbconn.close()
