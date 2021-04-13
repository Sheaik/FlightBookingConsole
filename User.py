from connection import mydb
from Administrator import Admin
#User's class
class Users():
    def viewFlights(self):
        ob1=Admin()
        ob1.listAllFlightSchedule()
    def bookFlight(self):
        allocatedSeats=0
        price=0
        Exit=0
        while(Exit!=-1):
            fId=int(input("pls, Enter the flightID you have to book:"))
            uId=int(input("pls, Enter the your UserID:"))
            mycursor=mydb.cursor()
            sql="SELECT * FROM flight WHERE FlightID="+str(fId)
            mycursor.execute(sql)
            myresult=mycursor.fetchall()
            for i in myresult:
                maxNoOfSeats=i[4]
                price=i[5]
                allocatedSeats=i[6]
            aseats=(allocatedSeats/maxNoOfSeats)*100
            if(aseats<50.0):
                pass
            elif(aseats<40.0 and aseats>10.0):
                tax=(price/100)*20
                price=price+tax
            else:
                tax=(price/100)*50
                price=price+tax
            if(allocatedSeats<maxNoOfSeats):
                mycursor=mydb.cursor()
                sql="INSERT INTO bookings(userId,FlightId,finalPrice) VALUES(%s,%s,%s)"
                val=(uId,fId,str(price))
                mycursor.execute(sql,val)
                mydb.commit()
                mycursor=mydb.cursor()
                allocatedSeats=allocatedSeats+1
                sql='UPDATE flight SET AllocatedSeats="'+str(allocatedSeats)+'"WHERE FlightID='+str(fId)
                mycursor.execute(sql)
                mydb.commit()
                ch=input("Do you want to book more?, say y or n")
                if(ch=='y' or ch=='Y'):
                    pass
                else:
                    Exit=-1
            else:
                print("Sorry Seats are not available :(")
                ch=input("Do you want to book another flight?, say y or n")
                if(ch=='y' or ch=='Y'):
                    pass
                else:
                    Exit=-1
    def viewAndCancelTickets(self):
        mycursor=mydb.cursor()
        print("Do you want to view")
        sql="SELECT * FROM bookings"
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        for i in myresult:
            print(i)
        ch=input("Do you want to cancel? say y or n")
        if(ch=='y' or ch=='Y'):
            Exit=0
            while(Exit!=-1):
                bid=int(input("Please Enter the booking ID:"))
                mycursor=mydb.cursor()
                sql='SELECT * FROM bookings WHERE BookingID='+str(bid)
                mycursor.execute(sql)
                result=mycursor.fetchall()
                for i in result:
                    fId=i[2]
                mycursor=mydb.cursor()
                sql='DELETE FROM bookings WHERE BookingId='+str(bid)
                mycursor.execute(sql)
                mydb.commit()
                mycursor=mydb.cursor()
                sql='SELECT * FROM flight'
                mycursor.execute(sql)
                result=mycursor.fetchall()
                for i in result:
                    allocatedSeats=i[6]
                allocatedSeats-=1
                mycursor=mydb.cursor()
                sql='UPDATE flight SET AllocatedSeats="'+str(allocatedSeats)+'"WHERE FlightID='+str(fId)
                mycursor.execute(sql)
                mydb.commit()
                ch=input("Do you want to cancel more? say y or n")
                if(ch=='n' or ch=='N'):
                    Exit=-1
        else:
            pass


           
        