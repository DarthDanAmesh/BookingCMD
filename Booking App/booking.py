# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 23:29:00 2021

@author: user
"""
import sqlite3

CREATE_PHONE_TBL = "CREATE TABLE IF NOT EXISTS phonebook (idn INTEGER PRIMARY KEY, name TEXT, number TEXT, datedata DATE, days INTEGER);"
INSERT_PHONETBLE = "INSERT INTO phonebook (name, number, datedata, days) VALUES (?,?,?,?);"
ALL_RECORDS = "SELECT * FROM phonebook;"
SELECT_NUMBER = "SELECT * FROM phonebook WHERE number =?;"
SELECT_NAME = "SELECT * FROM phonebook WHERE name=? ORDER BY DESC;"
SELCT_TOTAL_DAYS="SELECT * FROM phonebook WHERE days=? ORDER BY name DESC;"
#DELETE_NUMBER = "DELETE FROM phonebook WHERE idn =?;"


def connect():
    return sqlite3.connect("contacts.db")

def create_phonebook_tbl(connection):
    with connection:
        connection.execute(CREATE_PHONE_TBL)        

def add_record(connection, name, number, datedata, days):
    with connection:
        connection.execute(INSERT_PHONETBLE,(name, number, datedata, days,))
        
def select_all_records(connection):
    with connection:
        return connection.execute(ALL_RECORDS).fetchall()
        
def selct_by_name_number(connection, number):
    with connection:
        return connection.execute(SELECT_NUMBER, (number,)).fetchall()
        
def selct_by_name(connection, name):
    with connection:
        return connection.execute(SELECT_NAME, (name,))
        
def selct_totad_days(connection, number):
    with connection:
        return connection.execute(SELCT_TOTAL_DAYS, (number,)).fetchall()
    
def delete_record(connection, idn):
    with connection:
        return connection.execute("DELETE FROM phonebook WHERE idn =?;", [idn])
    
def retrieve_col(connection):
    with connection:
        c = connection.execute(connection.execute(ALL_RECORDS))
        print(c.description)