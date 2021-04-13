#for getting records from relation
from connection import mydb
#Administator's class
class Admin():
    def choose(self):
        mycursor=mydb.cursor()
        fId=int(input("Enter a flightID:"))
        mycursor.execute("SELECT * FROM flight WHERE FlightId= "+str(fId))
        myResult=mycursor.fetchall()
        for i in myResult:
            print(i)
        print("Do you want to change TakeOffTime? say y or n")
        ans=input()
        if(ans=='y' or ans=='Y'):
            takeOffTiming=input("Enter the TakeOffTime:")
            mycursor.execute('UPDATE flight SET TakeOffTiming= "'+takeOffTiming+'" WHERE FlightId= '+str(fId))
            mydb.commit()
        else:
            pass
        print("Do you want to change the price? say y or n")
        ans=input()
        if(ans=='y' or ans=='Y'):
            pricing=input("Enter the price of the ticket:")
            mycursor.execute('UPDATE flight SET Pricing= "'+pricing+'" WHERE FlightId= '+str(fId))
            mydb.commit()
        else:
            pass
        print("Do you want to change maxNoOfSeats? say y or n")
        ans=input()
        if(ans=='y' or ans=='Y'):
            maxNoOfSeats=input("Enter the MaxNoOfSeats:")
            mycursor.execute('SELECT * FROM flight')
            result=mycursor.fetchall()
            for i in result:
                allocatedSeats=i[6]
            if(int(maxNoOfSeats)<allocatedSeats):
                print("U can't do the operation!")
            else:
                mycursor.execute('UPDATE flight SET MaxNoOfSeats= "'+maxNoOfSeats+'" WHERE FlightId= '+str(fId))
                mydb.commit()

    def createAFlightSchedule(self):
        mycursor = mydb.cursor()
        sql="INSERT INTO  flight(Source,Destination,TakeOffTiming,MaxNoOfSeats,Pricing,AllocatedSeats) VALUES(%s,%s,%s,%s,%s,%s)"
        source=input("Enter the Source:")
        destination=input("Enter the Destination:")
        takeOffTiming=input("Enter the TakeOffTime:")
        maxNoOfSeats=int(input("Enter the MaxNoOfSeats:"))
        pricing=float(input("Enter the Price of the ticket:"))
        allocatedSeats=0
        val=(source,destination,takeOffTiming,maxNoOfSeats,pricing,allocatedSeats)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,"Record inserted.")  
        
    def listAllFlightSchedule(self):
        mycursor=mydb.cursor()
        mycursor.execute("SELECT * FROM flight")
        myresult = mycursor.fetchall()
        for i in myresult:
            print(i)
        print("All the flightSchedules have been listed")
    def updateSchedule(self):
        print("1.Enter a flightID")
        print("2.Display all and choose a flightId")
        ob=Admin()
        try:
            ch=int(input())
            if(ch==1):
                ob.choose()
            else:
                ob.listAllFlightSchedule()
                ob.choose()
        except:
            print("Please Enter a valid option!")
            
    def deleteSchedule(self):
        fId=int(input("Enter the flightId:"))
        mycursor=mydb.cursor()
        mycursor.execute("DELETE FROM bookings WHERE FlightId="+str(fId))
        mydb.commit()
        mycursor=mydb.cursor()
        mycursor.execute("DELETE FROM flight WHERE FlightId= "+str(fId))
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")