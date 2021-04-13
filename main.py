""" Python console program for flightBooking

    Backend:python
    DataBase:mySql
"""
from connection import mydb
from Administrator import Admin 
from User import Users
import getpass
import stdiomask
def admin():
    ob=Admin()
    Exit=0
    while(Exit!=-1):
        print("Choose an Available Operation listed below:")
        print("1.Create a Flight Schedule")
        print("2.List all Flight Schedule")
        print("3.Update Schedule")
        print("4.Delete Schedule")
        print("5.Exit")
        try:
            option=int(input())
            print("You have selected option %d"%option)
            if(option==1):
                ob.createAFlightSchedule()
            elif(option==2):
                ob.listAllFlightSchedule()
            elif(option==3):
                ob.updateSchedule()
            elif(option==4):
                ob.deleteSchedule()
            elif(option==5):
                Exit=-1
            else:
                print("Please Enter one of above listed options!!!")
        except:
            print("Enter a valid Number!")

#User Side
def user():
    ob=Users()
    Exit=0
    while(Exit!=-1):
        print("Choose an Available Operation listed below:")
        print("1.viewFlights")
        print("2.bookFlight")
        print("3.viewAndCancelTickets")
        print("4.Exit")
        try:
            option=int(input())
            print("You have selected option %d "%option)
            if(option==1):
                ob.viewFlights()
            elif(option==2):
                ob.bookFlight()
            elif(option==3):
                ob.viewAndCancelTickets()
            elif(option==4):
                Exit=-1
            else:
                print("Please Enter one of above listed options!!!")
        except:
            print("Enter a valid Number!")
        
            
#Main Method    
def main():
    Exit=0
    while(Exit!=-1):
        print("1.SignUP User")
        print("2.DisplayAll User")
        print("3. Admin")
        print("4. User")
        print("5. Exit")
        try:
            typeUser=int(input())
            print("You have selected option %d"%typeUser)
            if(typeUser==1):
                """
                create user panel
                """
                mycursor=mydb.cursor()
                sql="INSERT INTO user(role,username,password) VALUES(%s,%s,%s)"
                role=input("Enter the role of the user:")
                uname=input("Enter username:")
                pwd=stdiomask.getpass("Enter password:")
                val=(role,uname,pwd)
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount,"Record Inserted.")
            elif(typeUser==2):
                """
                display all user panel
                """
                mycursor=mydb.cursor()
                mycursor.execute("SELECT * FROM user")
                myResult=mycursor.fetchall()
                for i in myResult:
                    print(i)
            elif(typeUser==3):
                """
                Admin's Panel
                """
                print("Entered as a Admin!!!")
                ids=int(input("Enter the UserId"))
                mycursor=mydb.cursor()
                sql="SELECT * FROM user WHERE userId="+str(ids)
                mycursor.execute(sql)
                result=mycursor.fetchall()
                for i in result:
                    roles=i[1]
                    uName=i[2]
                    pWD=i[3]
                userName=input("Enter a username:")
                passwd=stdiomask.getpass("Enter a password:")#used stdiomasl for hiding input and convert it into asterisk(*)
                if(roles=="admin" and uName==userName and pWD==passwd):
                    print("Welcome "+uName+"!!!")
                    admin()
                else:
                    print("You doesn't have admin privileges!!!")
            elif(typeUser==4):
                """
                User's Panel
                """
                print("Entered as a User!!!")
                ids=int(input("Enter the UserId:"))
                username=input("Enter the username:")
                password=stdiomask.getpass("Enter the password:")
                mycursor=mydb.cursor()
                sql='SELECT * FROM user WHERE userId='+str(ids)
                mycursor.execute(sql)
                result=mycursor.fetchall()
                for i in result:
                    roles=i[1]
                    uName=i[2]
                    pWD=i[3]
                if(uName==username and pWD==password):
                    print("Welcome "+uName+"!!!")
                    user()
                else:
                    print("You are not registered passengers!!, Please Signup...")
            elif(typeUser==5):
                Exit=-1
            else:
                print("Please Enter one of above listed options!!!")
        except:
            print("Enter the valid option!!")

#calling of main()
main()