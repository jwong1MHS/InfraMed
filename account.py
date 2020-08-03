from mdb import *
from phone_calls import *

first_name = "Jason"
last_name = "Wong"
full_name = first_name + " " + last_name
phone_number = "+12027409056"
sid = "ACf13af826fa88d4d1b52e226f1a8fe178"
token = "d47eeb79017dc730811182330f4e57df"

def addPatient():
    print('- PATIENT INFORMATION -')
    print()
    last_name = input("Last name of patient? ").lower()
    first_name = input("First name of patient? ").lower()
    full_name = first_name + " " + last_name
    bday = input("Birthday of patient? (MM/DD/YYYY) ")
    insertPatient(last_name, first_name, bday)
    print()
    print('- CONTACT INFORMATION -')
    print()
    addContact(db.Patients.find_one({'last_name': last_name,
                                    'first_name': first_name,
                                    'birthday': bday}))
