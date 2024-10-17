#CONFIGURATION:
# font size - 8
# font - courier
# theme - dark
#----------------X--------X---------------------X
                 #[MODULE]#
#----------------X--------X---------------------X
"""
import subprocess
while True:
    try:
        import socket
        from datetime import datetime
        import time
        from pyfiglet import Figlet
        import sys
        from clrprint import *
        import tabulate
        import pymongo
        break
    except ModuleNotFoundError:
        modules_to_install = ['pyfiglet', 'clrprint', 'tabulate', 'pymongo']
        for module in modules_to_install:
            subprocess.check_call(['pip', 'install', module])"""
import socket
import threading
import queue
from datetime import datetime
import time
from pyfiglet import Figlet
import sys
from clrprint import *
import tabulate
import pymongo
#----------------X----------X---------------------X
                 #[DATABASE]#
#----------------X----------X---------------------X
try:
    client=pymongo.MongoClient("mongodb+srv://talkitive:class12proj@talkitive.0rpcz4p.mongodb.net/")
    db=client['talkitive']
    db["Registration"].create_index("Username", unique=True)
except pymongo.errors.ConnectionFailure:
    clrprint("Failed to connect to database",clr="red")
#----------------X----------X---------------------X
                 #[FUNCTIONS]#
#----------------X----------X---------------------X
def EXIT(variable=None):
    if variable is not None and variable.lower() == 'exit':
        print_with_typing("Exiting...",0.05)
        sys.exit(0)
    else:
        print_with_typing("Exiting...",0.05)
        sys.exit(0)
def MENU():
    return 
def MSG():
    pass

def SEARCH():
    pass
#----------------X--------------X---------------------X
                 #[REGISTRATION]#
#----------------X--------------X---------------------X
def has_special_char(name):
    special_char = "!@#$%^&*()_+{}:\"<>?|\/'[]~`"
    for char in name:
        if char in special_char:
            return True

def has_digits(name):
    for char in name:
        if char.isdigit():
            return True

def Registration():
    clrprint(Figlet(font='banner3-d', width=115).renderText("REGISTRATION:"),clr='yellow')
    def valid_name():
        name="notexit"
        validation=False
        while True:
            try:
                name = input("Enter your name: ")
                if name.lower()=='exit':
                    EXIT()
                if not has_special_char(name) and not has_digits(name):
                    validation=True
                    return name
                else:
                    print("Invalid name. Name cannot contain special characters or digits.\n")
            except KeyboardInterrupt:
                print("I dont think you intended to do that.\nif you want to exit then exit by typing exit..sooo simple\n")
    
    def UserName():
        def user(name):
            special_char = "!@#$%^&*()+{}:\"<>?|\/'[]~`"
            for char in name:
                if char in special_char:
                    return False
        while True:
            try:
                name=input("Enter a Username: ")
                name=name.lower()
                column_name="Username"
                allusernames = []
                for document in db["Registration"].find({}, {column_name: 1, "_id": 0}):
                    if column_name in document:
                        allusernames.append(document[column_name])
                if name.lower()=='exit':
                    EXIT()
                if not user(name) and len(name)>4:
                    if name not in allusernames:
                        return name
                    else:
                        clrprint("You are late.... Username is taken, try another one!!",clr="red")
                else:
                    print("Invalid Username. Username should be more than 4 characters and can only contain digits, underscores and alphabets!.\n")
                
            except KeyboardInterrupt:
                print("I dont think you intended to do that.\nif you want to exit then exit by typing exit..sooo simple\n")
    
    def Password():
        while True:
            try:
                name = input("Enter Password: ")
                if name.lower()=='exit':
                    EXIT()
                passtren=False
                for i in name:
                    if i.isupper():
                        passtren=True
                if has_special_char(name) and has_digits(name) and passtren and len(name)>=7:
                    return name
                else:
                    print("Password should be minimum of 7 characters, contain special characters,digits and atleast 1 Capital letter.\n")
            except KeyboardInterrupt:
                print("I dont think you intended to do that.\nif you want to exit then exit by typing exit..sooo simple\n")
    Error=True
    while Error:
        try:
            new_document = {
            "Serial_no": db["Registration"].find_one({}, sort=[("Serial_no", pymongo.DESCENDING)])["Serial_no"]+1,
            "Timestamp":datetime.now(),
            "Local_Ip": ip_address(),
            "Name": valid_name(),
            "Username": UserName(),
            "Password": Password(),
            "Block_status": False,
            "Useragreement": UserAgreement()
            }
            db["Registration"].insert_one(new_document)
            print()
            print_with_typing("Successfully Registered!!",0.04)
            Error=False
        except pymongo.errors.DuplicateKeyError:
            Error = True
            clrprint("Username already exists choose another one",clr="red")
    clrprint("=============================X===================================X========================================X\n=============================X===================================X========================================X",clr="green")
#----------------X-------X---------------------X
                 #[LOGIN]#
#----------------X-------X---------------------X
def Login():
    #socket.gethostbyname(socket.gethostname()) TO BE USED when logged in
    clrprint(Figlet(font='banner3-d').renderText("LOGIN:"),clr='yellow')
    wrong=0
    match=False
    username="default"
    password="default"
    while match==False and (username.lower()!='exit' or password.lower()!='exit'):
        try:
            username = input("Enter Your Username: ").lower()
            if username.lower()=='exit':
                EXIT()
            password = input("Enter Your Password: ")
            if password.lower()=='exit':
                EXIT()
                clrprint("=============================X===================================X========================================X",clr="red")
            if wrong==5:
                wrong=1
                print_with_typing("6 Wrong attempts....U need to wait for 5 Seconds before trying again!...",0.05)
                for i in range(5,0,-1):
                    time.sleep(0.5)
                    print("wait for",i," seconds")
            elif db["Registration"].find_one({"Username": username}) and db["Registration"].find_one({"Password":password}):
                match=True
                if not (db["Registration"].find_one({"Username":username})["Block_status"] and db["Registration"].find_one({"Local_Ip":ip_address()})["Block_status"]):
                    tries=0
                    while db["Registration"].find_one({"Username":username})["Useragreement"] == False :
                        if tries!=3:
                            db['Registration'].update_one({"Username":username},{"$set":{"Useragreement":UserAgreement()}})
                            tries+=1
                        else:
                            EXIT()
                        
                    if tries==3:
                        text="AUTO-CLOSING..."
                        print_with_typing(text, delay=0.04)
                        sys.exit()   
                    new_document = {
                    "Serial_no": db["Login"].find_one({}, sort=[("Serial_no", pymongo.DESCENDING)])["Serial_no"]+1,
                    "Timestamp":datetime.now(),
                    "Local_Ip": ip_address(),
                    "Username":username}
                    db["Login"].insert_one(new_document)
                    chat(username)
                else:
                    clrprint("You have been blocked by the admin, please contact the administrator",clr="red")
            else:
                clrprint("\tIncorrect Username/Password!!",clr="red")
                wrong+=1
        except KeyboardInterrupt:            
            print("I dont think you intended to do that.\nif you want to exit then exit by typing exit..sooo simple\n")
#----------------X-------------X---------------------X
                 #[CHAT-SCREEN]#
#----------------X-------------X---------------------X
message_queue = queue.Queue()
def display_messages():
    mycollection = db["Chat"]
    fields = {"_id": 0, "Sender": 1, "Message": 1}
    change_stream = mycollection.watch()
    
    while True:
        for change in change_stream:
            if change["operationType"] == "insert":
                message_queue.put(change["fullDocument"])
        
        while not message_queue.empty():
            message = message_queue.get()
            clrprint(Figlet(font='banner3-d').renderText("INBOX"), clr='green')
            print("New message received:")
            print("Sender:", message["Sender"])
            print("Message:", message["Message"])
            print("-" * 30)
        
        time.sleep(2)

def message(username):
    mycollection = db["Chat"]
    msg = ""
    
    while True:
        msg = input("\nMessage: ")
        new_document = {
            "Serial_no": db["Login"].find_one({}, sort=[("Serial_no", pymongo.DESCENDING)])["Serial_no"]+1,
            "Timestamp":datetime.now(),
            "Local_Ip": ip_address(),
            "Sender":username,
            "Message":msg
            }
        if msg.lower()=="menu":
            inp=input("Do you want to exit to the menu?(Y/N): ")
            if inp in "yesYes":
                MENU()
            else:
                pass
        elif msg.lower()=="exit":
            inp=input("Do you want to exit?(Y/N): ")
            if inp in "yesYes":
                EXIT()
            else:
                pass
        else:
            mycollection.insert_one(new_document)
            message_queue.put(new_document)
            
def chat(username):
    mycollection = db["Chat"]
    all_documents = mycollection.find()
    msg=""
    first=True
    change_stream = mycollection.watch()
    disthread=threading.Thread(target=display_messages)
    dis1thread=threading.Thread(target=message,args=(username,))
    disthread.start()
    dis1thread.start()
    
    """while msg.lower()!="exit" or msg.lower()!="menu":
        fields={"_id":0,"Sender":1,"Message":1}
        data = [document for document in db["Chat"].find({},fields)]
        print()
        if first:
                clrprint(Figlet(font='banner3-d').renderText("INBOX"),clr='green')
                print(tabulate.tabulate(data, headers="keys", tablefmt="grid"))
                msg=input("Message: ")
                new_document = {
                    "Serial_no": db["Login"].find_one({}, sort=[("Serial_no", pymongo.DESCENDING)])["Serial_no"]+1,
                    "Timestamp":datetime.now(),
                    "Local_Ip": ip_address(),
                    "Sender":username,
                    "Message":msg
                    }
                if msg.lower()=="menu":
                    inp=input("Do you want to exit to the menu?(Y/N): ")
                    if inp in "yesYes":
                        MENU()
                    else:
                        pass
                elif msg.lower()=="exit":
                    inp=input("Do you want to exit?(Y/N): ")
                    if inp in "yesYes":
                        EXIT()
                    else:
                        pass
                else:
                    mycollection.insert_one(new_document)
                #first=False
        
        for change in change_stream:
            if change["operationType"] == "insert":
                data = [document for document in db["Chat"].find({},fields)]
                clrprint(Figlet(font='banner3-d').renderText("INBOX"),clr='green')
                print(tabulate.tabulate(data, headers="keys", tablefmt="grid"))
                msg=input("Message: ")
                new_document = {
                    "Serial_no": 0,
                    "Timestamp":datetime.now(),
                    "Local_Ip": ip_address(),
                    "Sender":username,
                    "Message":msg
                    }
                if msg.lower()=="menu":
                    inp=input("Do you want to exit to the menu?(Y/N): ")
                    if inp in "yesYes":
                        MENU()
                    else:
                        pass
                elif msg.lower()=="exit":
                    inp=input("Do you want to exit?(Y/N): ")
                    if inp in "yesYes":
                        EXIT()
                    else:
                        pass
                else:
                    mycollection.insert_one(new_document)"""
            
    
    #should print existing chats
#----------------X-------------------X---------------------X
                 #[LICENSE-AGREEMENT]#
#----------------X-------------------X---------------------X
def UserAgreement():
    usans="NoNOPEno"
    print("\n\t\tTERMS AND CONDITIONS")
    clrprint("""
By using this Python program, you agree to the following terms and conditions. Please read them carefully before proceeding:

1. Responsible Use:
You agree to use this program responsibly and for lawful purposes only. You will not engage in any illegal, harmful, or malicious activities using this program.

2. Program Intended Use:
This program is designed to create safe environment. It should be used solely for its intended purpose by obeying the norms of society.

3. User's Responsibility:
Any message sent on this chat is the sole responsibility of the user. The owner of the program shall not be held liable for any message sent or recieved.

4. Compliance with Laws:
You agree to comply with all applicable laws, regulations, and legal requirements in your jurisdiction while using this program.

5. Indemnification:
You agree to indemnify and hold harmless the owner of the program from any claims, damages, or liabilities arising out of your use or misuse of the program.

6. Acceptance of Terms:
By using this program, you acknowledge that you have read, understood, and accepted these terms and conditions in their entirety.

If you do not agree with any part of these terms and conditions, you cannot not proceed with the use of this program.
=============================X===================================X========================================X\n=============================X===================================X========================================X""",clr="green")
    usans=input("Do you agree to the terms and conditions?(Y/N): ")
    if usans in "YESyesyep":
        print("Now that you have agreed to the terms and conditions....here is your account")
        return True
    else:
        text=" You cannot use this program without agreeing."
        print_with_typing(text, delay=0.04)
        return False
#----------------X-----------------X---------------------X
                 #[OTHER FUNCTIONS]#
#----------------X-----------------X---------------------X
def ip_address():
    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.error:
        return None
def banner():
    ascii_art = Figlet(font='larry3d', width=100).renderText("Talkitive")
    clrprint(ascii_art,clr='red')
    
def print_with_typing(text, delay):
    for char in text:
        print(char, end='')  
        time.sleep(delay)  
    print()

functions=['EXIT','MSG','SEARCH']
def main():
    banner()
    print("""    +--------------------------------------------------------------------------------------------+
    |\tThis is a python program for people like us to chat accross the classroom.               |  
    |\tthis project has been made maximum bug free but you can still come across any bug...     |
    +--------------------------------------------------------------------------------------------+""")
    userans=""
    while userans.upper() not in ['2','3','4']:
        try:
            clrprint(Figlet(font='banner3-d', width=115).renderText("Menu:"),clr='green')
            print("""\n
        1) REGISTER 
        2) LOGIN
        3) Help
        4) Exit""")
            userans=input("\nEnter your desired choice from the Menu: ")
            clrprint("=============================X===================================X========================================X\n=============================X===================================X========================================X",clr="green")
            if userans.upper() not in ['1','2','3','4',"REGISTER","LOGIN","HELP","EXIT"]:
                clrprint("Please stick to the options provided in the menu!!",clr='red')
            elif userans.upper()=="EXIT":
                EXIT()
            elif userans=='1' or userans.upper()=="REGISTER":
                Registration()
            print()
        except KeyboardInterrupt:
            
            clrprint("=============================X===================================X========================================X\n=============================X===================================X========================================X",clr="green")
            print("I dont think you intended to exit like that....\n\n")
            
    if userans=='2' or userans.upper()=="LOGIN":
        Login()
    elif userans=='3' or userans.upper()=="HELP":
        pass #show all functions and stuff
    elif userans=='4' or userans.upper=="EXIT":
        EXIT()
#----------------X-------------X-----------------X
                 #[MAIN _ BODY]#
#----------------X-------------X-----------------X
main()
