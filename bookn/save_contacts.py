# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 23:31:24 2021

@author: user
"""
import booking
import sys

OPTIONS_MENU = """
-------------------BOOKING STORE-------------------

1. Create Booking
2. View Bookings
3. Search for a Booking
4. Delete a Booking
6. View Table Columns
5. Exit Program

What is your selection?: """

RECORDS_IN_THE_DATABASE = """
-------------------BOOKING STORE-------------------

"""

        
def see_menu():
    connection = booking.connect()
    booking.create_phonebook_tbl(connection)
    while True:
        user_input = input(OPTIONS_MENU)
        if user_input == "5":
            sys.exit("Exiting, see ya!")
        elif user_input =="1":
            name=input("Enter Booking Name: ")
            number=input("Enter Phone Number: ")
            datedata=input("Enter Booking Date: ")
            days=int(input("Enter Duration of Stay: "))
            
            booking.add_record(connection, name, number, datedata, days)
            
        elif user_input =="2":
            records = booking.select_all_records(connection)
            for record in records:
                print(record)
                
        elif user_input =="3":
            name=input("Enter Booking Name: ")
            booking.selct_by_name(connection, name)
            
        elif user_input =="4":
            print(RECORDS_IN_THE_DATABASE)
            records = booking.select_all_records(connection)
            for record in records:
                print(record)
                
            print()
            number=int(input("Select the unique ID Number: "))
            booking.delete_record(connection, number)
            
        elif user_input =="6":
            return booking.retrieve_col(connection)
see_menu()
