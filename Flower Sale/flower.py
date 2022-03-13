import sqlite3

class flower():
    def __init__(self):
        self.connectdatabase()
        self.status=True
    def run(self):
        choice=self.menuchoice()
        if choice==1:
            kindofflower = self.kindofflower()
            numberofflowers=self.numberofflowers()
            self.cursor.execute("SELECT number FROM flowers WHERE rowid={}".format(kindofflower))
            currentnumber = self.cursor.fetchall()[0][0]
            latestnumber=currentnumber+numberofflowers
            self.cursor.execute("UPDATE flowers SET number={} WHERE rowid={}".format(latestnumber,kindofflower))
            self.connect.commit()
            if kindofflower==1:
                earning=latestnumber*0.5
                self.cursor.execute("UPDATE flowers SET earning={} WHERE rowid={}".format(earning,kindofflower))
                self.connect.commit()
            if kindofflower==2:
                earning=latestnumber*0.6
                self.cursor.execute("UPDATE flowers SET earning={} WHERE rowid={}".format(earning,kindofflower))
                self.connect.commit()
            if kindofflower==3:
                earning=latestnumber*0.7
                self.cursor.execute("UPDATE flowers SET earning={} WHERE rowid={}".format(earning,kindofflower))
                self.connect.commit()
        if choice==2:
            self.finish()
    def menuchoice(self):
        select=int(input("""
        *** Select your choice ***
        1)Add selling flower 
        2)Exit system
        """))
        return select
    def numberofflowers(self):
        numberofflower=int(input("How many flowers have you sold?"))
        return numberofflower
    def kindofflower(self):
        while True:
            try:
                kindofflower=int(input("1)Carnation\n2)Poppy\n3)Rose"))
                while kindofflower<1 or kindofflower>3:
                    kindofflower=int(input("Please enter a number between 1-3."))
                break
            except ValueError:
                print("Enter a number between 1-3")
        return kindofflower
    def connectdatabase(self):
        self.connect=sqlite3.connect("Flower.db")
        self.cursor=self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS flowers(kind TEXT,number INT,earning INT)")
        self.connect.commit()
    def addflowernames(self):
        self.cursor.execute("INSERT  INTO  flowers VALUES ('carnation',0,0)")
        self.cursor.execute("INSERT  INTO  flowers VALUES('poppy',0,0)")
        self.cursor.execute("INSERT  INTO flowers VALUES ('rose',0,0)")
        self.connect.commit()
    def finish(self):
        self.status=False

market=flower()
market.addflowernames()
while market.status:
    market.run()
