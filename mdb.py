from pymongo import MongoClient

# connect to MongoDB
client = MongoClient('mongodb+srv://dsalmanowitz:eldercare@cluster0.rpfik.mongodb.net/Cluster0?retryWrites=true&w=majority')
db=client.Users

#Add Data

def insertContact(last, first, num, relation, response):
    db.Contacts.insert_one(
        { 'last_name' : last,
          'first_name' : first,
          'phone_number' : num:
          'relation' : relation
          'response_type' : response
          })
def insertPatient(last, first, age):
    db.Patients.insert_one(
        { 'last_name' : last,
          'first_name' : first,
          'age' : age
          })
