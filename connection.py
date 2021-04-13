#C:\Users\sheaik\AppData\Local\Programs\Python\Python39
"""
bookinng is the name of the database

It contains 3 relation namely:
                *flight
                *user
                *booking
1.flight relation contains following attributes:
                flightId (int)(primary key)(Auto_Increment),
                source(string),
                destination(string),
                takeOffTiming(string),
                maxNoofSeats(int),
                pricing(float),
                allocatedSeats(based on which we calculate final price and validations).
2.user relation contains following attributes:
                userID(int)(primary key)(Auto_Increment),
                role (String),
                username(string),
                password(string).
3.Booking relation contains following attributes:
                BookingId (int) (primary Key) (Auto_Increment),
                userId (int) 
                flightId (int) 
                pricing(string).
"""
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="flightBookingConsole")

mycursor=mydb.cursor()


