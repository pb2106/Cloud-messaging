
import pymongo
from tabulate import tabulate
from datetime import datetime
client = pymongo.MongoClient("your mongodb connection string")
db = client['talkitive']
###
print("""PYMONGO - DB ADMIN""")
#mycollection = mydb.table1
# Data to be inserted as a list of dictionaries
"""Insert data into the collection using insert_many"""
#adding to table - mycollection.insert_many(rec)
#print((db["Registration"].find_one({"Username":"naeglaria_fowleri"})["Block_status"] and db["Registration"].find_one({"Local_Ip":"192.168.226.1"})["Block_status"]))
"""getting all collection names"""
#collection_names = db.list_collection_names()

"""Print the collection names"""
#print(collection_names)

""" DELETE COLLECTION """
#mydb["table1"].drop()
print("""MENU:
1) Print All collections
2) create a collection
3) delete a collection
4) adding data into collection
5) print all data
6) delete a record
7) block/unblock an ip
8) delete all records
9) update message""")
userinp = input("What do u wanna do?: ")
if userinp in ['1','2','3','4','5','6','7','8','9']:
    if userinp=='1':
        collection_names = db.list_collection_names()
        print(collection_names)
    elif userinp=='2':
        name=input("Enter a name to create a collection: ")
        db.create_collection(name)
        print("Collection",name,"Created")
    elif userinp=='3':
        collection_names = db.list_collection_names()
        print("BELOW ARE THE AVAILABLE COLLECTIONS...\n",collection_names)
        name=input("Enter collection name to delete: ")
        db[name].drop()
        print(name,"Deleted")
        
    elif userinp=='4':
        collection_names = db.list_collection_names()
        print("""BELOW ARE THE AVAILABLE COLLECTIONS...
you can choose from below or give ur own name to create a collection\n""",collection_names)
        name=input("Enter collection to add data: ")
        if name=="Registration":
            new_document = {
            "Serial_no": 0,
            "Timestamp":datetime.now(),
            "Local_Ip": "0.0.0.0",
            "Name": "Admin",
            "Username": "Admin",
            "Password":"Admins123",
            "Block_status": False,
            "Useragreement": True
            }
        elif name=="Login":
            new_document = {
            "Serial_no": 0,
            "Timestamp":datetime.now(),
            "Local_Ip": "0.0.0.0",
            "Username":"Admin"}
        #print(db[name].find_one({}, sort=[("Serial_no", pymongo.DESCENDING)])["Serial_no"]+1)
        
        elif name=="Chat":
            new_document = {
            "Serial_no": 0,
            "Timestamp":datetime.now(),
            "Local_Ip": "0.0.0.0",
            "Sender":"Admin",
            "Message":"Welcome People, Be friendly and listen to class."}

        mycollection = db[name]
        mycollection.insert_one(new_document)
        print("data added")
    elif userinp=='5':
        collection_names = db.list_collection_names()
        print("""BELOW ARE THE AVAILABLE COLLECTIONS...\n""",collection_names)
        name=input("Enter collection to view data: ")
        mycollection = db[name]
        all_documents = mycollection.find()
        data = [document for document in all_documents]
        print(tabulate(data, headers="keys", tablefmt="grid"))

    elif userinp=='6':
        collection_names = db.list_collection_names()
        print("""BELOW ARE THE AVAILABLE COLLECTIONS...\n""",collection_names)
        name=input("Enter collection to view data: ")
        mycollection = db[name]
        all_documents = mycollection.find()
        data = [document for document in all_documents]
        print(tabulate(data, headers="keys", tablefmt="grid"))
        no=int(input("Enter serial num to delete: "))
        db[name].delete_one({"Serial_no": no})
        data=[document for document in db[name].find()]
        print(tabulate(data, headers="keys", tablefmt="grid"))
    elif userinp=='7':
        collection_names = db.list_collection_names()
        print("""BELOW ARE THE AVAILABLE COLLECTIONS...\n""",collection_names)
        name=input("Enter collection to view data: ")
        all_documents = db[name].find()
        data = [document for document in all_documents]
        print(tabulate(data, headers="keys", tablefmt="grid"))
        no=int(input("Enter serial num : "))
        task=input("block or unblock: ")
        if task.lower()=="block":
            result = db[name].update_one({"Serial_no":no},{"$set":{"Block_status":True}})
            if result.modified_count == 1:
                print("Successfully blocked")
            else:
                print("error")
        elif task.lower()=='unblock':
            result = db[name].update_one({"Serial_no":no},{"$set":{"Block_status":False}})
            if result.modified_count == 1:
                print("Successfully unblocked")
            else:
                print("error")
    elif userinp=='8':
        collection_names = db.list_collection_names()
        print("""BELOW ARE THE AVAILABLE COLLECTIONS...\n""",collection_names)
        name=input("Enter collection to view data: ")
        mycollection = db[name]
        all_documents = mycollection.find()
        data = [document for document in all_documents]
        print(tabulate(data, headers="keys", tablefmt="grid"))
        i=1
        filter = {"Serial_no": {"$gt": 0}}
        mycollection.delete_many(filter)
        data=[document for document in db[name].find()]
        print(tabulate(data, headers="keys", tablefmt="grid"))
    elif userinp=='9':
        collection_names = db.list_collection_names()
        print("""BELOW ARE THE AVAILABLE COLLECTIONS...\n""",collection_names)
        name=input("Enter collection to view data: ")
        all_documents = db[name].find()
        data = [document for document in all_documents]
        print(tabulate(data, headers="keys", tablefmt="grid"))
        no=int(input("Enter serial num : "))
        result = db[name].update_one({"Serial_no":no},{"$set":{"Message":"Welcome People, Be friendly and listen to class."}})
else:
    print("ENTER FROM THE MENU")







        
