import pymongo
def insert_document(collection):
    document = {"name": name, "age":age, "race":race}
    collection.insert_one(document)
    print("document inserted")
def find_document(collection):
    myage= collection.find({"age":age},{"name":1, "_id":0})
    for ape in myage:
        print(ape["name"])

def update_document(collection):
   collection.update_one({"name":name},{"$set":{"age":age}})
   for doc in collection.find({"name": name}):
       print(doc)                                         
def delete_document(collection):
    collection.delete_many({"name": name})
    print("document deleted")

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["test_database"]
    collection = db["test_collection"]
    user_input = input("Enter 1 to insert, 2 to find, 3 to update, 4 to delete:")
    if user_input == '1':
        name= input("Enter name:")
        age= int(input("Enter age:"))
        race= input("Enter race:")
        insert_document(collection)
    elif user_input == '2':
        age= int(input("Enter age:"))
        find_document(collection)
    elif user_input == '3':
        name= input("Enter name:")
        age= int(input("Enter age:"))
        race= input("Enter race:")
        update_document(collection)
    elif user_input == '4':
        name= input("Enter name:")
        delete_document(collection)       

    