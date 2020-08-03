# must be run on the internet
# will not work with trial accounts
from twilio.rest import Client
from mdb import *
#from account import *

account_sid = "ACf13af826fa88d4d1b52e226f1a8fe178"
# Authentication token may constantly change
auth_token  = "d47eeb79017dc730811182330f4e57df"

client = Client(account_sid, auth_token)

callContacts = []
messageContacts = []

def addCalls(contact_number):
  call = client.calls.create(
      to=contact_number,
      from_=phone_number,
      url="http://demo.twilio.com/docs/voice.xml")
  message = client.messages.create(
      to=contact_number, 
      from_=phone_number,
      body=full_name + " has added you as an emergency contact for our InfraMed program. You will receive a call from this number if " + full_name + " has an emergency.")
  print(call.sid)
  print(message.sid)
  # add confirmation to be used as contact
  addAnotherContact()

def addMessages(contact_number):
  message = client.messages.create(
      to=contact_number, 
      from_=phone_number,
      body=full_name + " has added you as an emergency contact for our InfraMed program. You will receive an SMS message from this number if " + full_name + " has an emergency.")
  print(message.sid)
  # add confirmation to be used as contact
  addAnotherContact()

def addBoth(contact_number):
  message = client.messages.create(
      to=contact_number, 
      from_=phone_number,
      body=full_name + " has added you as an emergency contact for our InfraMed program. You will receive both a call and an SMS message from this number if " + full_name + " has an emergency.")
  # add confirmation to be used as contact
  print(message.sid)
  addAnotherContact()

def addContact(pat_id = None):
  lastname = input("Last name of contact? ").lower()
  firstname = input("First name of contact? ").lower()
  contact_number = input("Number of contact? ").lower()
  contact_relation = input("Relation to contact? ").lower()
  contact_type = input("Call or message or both? ").lower()

  if contact_type == "call" or contact_type == "calls":
    callContacts.append([lastname, firstname, contact_number, contact_relation])
    insertContact(lastname, firstname, contact_number, contact_relation, "call", pat_id)
    addCalls(contact_number)
  elif contact_type == "message" or contact_type == "messages":
    messageContacts.append([lastname, firstname, contact_number, contact_relation])
    insertContact(lastname, firstname, contact_number, contact_relation, "message", pat_id)
    addMessages(contact_number)
  elif contact_type == "both":
    callContacts.append([lastname, firstname, contact_number, contact_relation])
    messageContacts.append([lastname, firstname, contact_number, contact_relation])
    insertContact(lastname, firstname, contact_number, contact_relation, "both", pat_id)
    addBoth(contact_number)
  else:
    addContact()

def addAnotherContact():
  addcontact = input("Add another contact (yes or no)? ")
  if addcontact.lower() == "yes":
    addContact()
  elif addcontact.lower() == "no":
    print(callContacts)
    print(messageContacts)
  else:
    addAnotherContact()
