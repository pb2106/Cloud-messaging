#----------------X---------X---------------------X
                 #[MODULES]#
#----------------X---------X---------------------X
import subprocess
done=True
while done:
    try:
        from tkinter import *
        import tkinter as tk
        import tkinter.messagebox
        import socket
        import sys
        import pymongo
        from tabulate import tabulate
        from datetime import datetime
        import time
        import threading
        done=False
        break
    except ModuleNotFoundError:
        modules_to_install = ['tk', 'pymongo','tabulate']
        for module in modules_to_install:
            subprocess.check_call(['pip', 'install', module])
#----------------X----------X---------------------X
                 #[DATABASE]#
#----------------X----------X---------------------X
try:
    client=pymongo.MongoClient("mongodb+srv://talkitive:class12proj@talkitive.0rpcz4p.mongodb.net/")
    db=client['talkitive']
    db["Registration"].create_index("Username", unique=True)
    collection=db["Registration"]
except pymongo.errors.ConnectionFailure:
    tkinter.messagebox.showinfo("Connection Error!","ERROR CONNECTING TO DATABASE")
    sys.exit(0)
window = tk.Tk()
#----------------X----------X---------------------X
                 #[FUNCTIONS]#
#----------------X----------X---------------------X
def destroy():
    window.destroy()

def main():
    global window
    window.geometry("600x450")
    window.title("Login and Signup system")
    
    label1 = Label(window, text="REGISTER OR LOGIN!", font="times 20")
    label1.grid(row=3, column=3, columnspan=2)

    button1 = Button(window, text="Login", width=20, command=login)
    button1.grid(row=5, column=3)

    button2 = Button(window, text="Signup", width=20, command=signup)
    button2.grid(row=5, column=4)

    button3 = Button(window, text="Exit", width=20, command=destroy)
    button3.grid(row=6, column=4)
#----------------X-------X---------------------X
                 #[LOGIN]#
#----------------X-------X---------------------X    
def login():
    window.withdraw()
    global login_window
    login_window = tk.Toplevel(window)  
    login_window.title("Login")  
    login_window.geometry("600x650")  

    l1 = Label(login_window, text="Username: ", font="times 20")
    l1.grid(row=1, column=0)

    l2 = Label(login_window, text="Password: ", font="times 20")
    l2.grid(row=2, column=0)

    l3 = Label(login_window, font="times 20")
    l3.grid(row=5, column=1)

    username_text = StringVar()
    e1 = Entry(login_window, textvariable=username_text)
    e1.grid(row=1, column=1)
    
    password_text = StringVar()
    e2 = Entry(login_window, textvariable=password_text, show='*')
    e2.grid(row=2, column=1)
    def login_back():
        login_window.destroy()    
        window.deiconify()
    def loginn():
        def ip_address():
            try:
                return socket.gethostbyname(socket.gethostname())
            except socket.error:
                return None
        username_text1=username_text.get()
        password_text1=password_text.get()
        
        mycollection = db["Registration"]
        fields = {"_id": 0, "Username":1, "Password":1}
        all_documents = mycollection.find({}, fields)
        data = [document for document in all_documents]
        cred=[]
        for i in data:
            cred.append(list(i.values()))

        for i in cred:
            if username_text1 in i and password_text1 in i:
                match=True
                if not (db["Registration"].find_one({"Username":username_text1})["Block_status"] and db["Registration"].find_one({"Local_Ip":ip_address()})["Block_status"]):
                    new_document = {
                    "Serial_no": db["Login"].find_one({}, sort=[("Serial_no", pymongo.DESCENDING)])["Serial_no"]+1,
                    "Timestamp":datetime.now(),
                    "Local_Ip": ip_address(),
                    "Username":username_text1}
                    #db["Login"].insert_one(new_document)
                    
                    login_window.destroy()
                    tkinter.messagebox.showinfo("Logged in!","Login Successful!")
                    if username_text1=="Admin":
                        adminchat(username_text1)# ADMIN chat screen
                        break
                    else:
                        chat(username_text1)# normal user chat screen
                        break
                else:
                    tkinter.messagebox.showinfo("Banned!","You have been blocked by the admin, please contact the administrator")
                    login_window.destroy()
                    break
        else:
            tkinter.messagebox.showinfo("WRONG CREDENTIALS!!","Incorrect Username/Password!!")
            
    b = Button(login_window, text="Login", width=20, command=loginn)
    b.grid(row=4, column=1)
    
    b1 = Button(login_window, text="Back", width=20, command=login_back)
    b1.grid(row=4,column=2)
    login_window.mainloop()
#----------------X--------------X---------------------X
                 #[REGISTRATION]#
#----------------X--------------X---------------------X    
def signup():
    window.withdraw()
    global signup_window
    signup_window = tk.Toplevel(window)
    signup_window.geometry("800x650")
    signup_window.title("Sign Up")

    l1 = Label(signup_window, text="Name: ", font="times 20")
    l1.grid(row=1, column=1)

    l2 = Label(signup_window, text="Username: ", font="times 20")
    l2.grid(row=2, column=1)

    l3 = Label(signup_window, text="Password: ", font="times 20")
    l3.grid(row=3, column=1)
    
    l4 = Label(signup_window, text="Do you accept useragreement? tick the checkbox to accept", font="times 15")
    l4.grid(row=5, column=1)

    l5 = Label(signup_window,text="Password should be a minimum of 7 characters, contain special characters, digits, and at least 1 capital letter", font="times 8")
    l5.grid(row=4,column=1)
    
    name_text = StringVar()
    e1 = Entry(signup_window, textvariable=name_text)
    e1.grid(row=1, column=2)

    username_text = StringVar()
    e2 = Entry(signup_window, textvariable=username_text)
    e2.grid(row=2, column=2)

    password_text = StringVar()
    e3 = Entry(signup_window, textvariable=password_text, show='*')
    e3.grid(row=3, column=2)

    agree_text = IntVar()
    e4 = Checkbutton(signup_window,text=" ",variable=agree_text)
    e4.grid(row=5, column=2)

    def signup_back():
        signup_window.destroy()    
        window.deiconify()
#----------------X-------------------X---------------------X
                 #[LICENSE-AGREEMENT]#
#----------------X-------------------X---------------------X    
    def UserAgreement():
        tkinter.messagebox.showinfo("Useragreement","""
       By using this Python program, you agree to the following terms and conditions. Please read them carefully before proceeding:

    1. Responsible Use:
    You agree to use this program responsibly and for lawful purposes only. You will not engage in any illegal, harmful, or malicious activities using this program.

    2. Program Intended Use:
    This program is designed to create safe environment. It should be used solely for its intended purpose by obeying the norms of society.

    3. User\'s Responsibility:
    Any message sent on this chat is the sole responsibility of the user. The owner of the program shall not be held liable for any message sent or recieved.

    4. Compliance with Laws:
    You agree to comply with all applicable laws, regulations, and legal requirements in your jurisdiction while using this program.

    5. Indemnification:
    You agree to indemnify and hold harmless the owner of the program from any claims, damages, or liabilities arising out of your use or misuse of the program.

    6. Acceptance of Terms:
    By using this program, you acknowledge that you have read, understood, and accepted these terms and conditions in their entirety.

    If you do not agree with any part of these terms and conditions, you cannot not proceed with the use of this program.""")

    b2 = Button(signup_window, text="USER-AGREEMENT", width=20, command=UserAgreement)
    b2.grid(row=4, column=3)
    def signupp():
        def has_special_char_user(name_text):
            special_char = "!@#$%^&*()_+{}:\"<>?|/'[]~` "
            for char in name_text:
                if char in special_char:
                    return True
            return False
        def has_special_char(name_text):
            special_char = "!@#$%^&*()_+{}:\"<>?|/'[]~` "
            for char in name_text:
                if char in special_char:
                    return True
            return False

        def has_digits(name_text):
            for char in name_text:
                if char.isdigit():
                    return True
            return False
        
        def valid_name(name_text):
                if not has_special_char(name_text) and not has_digits(name_text) and name_text != "":
                    return name_text
                else:
                    tkinter.messagebox.showinfo("Invalid Name", "Name should not contain special characters or digits")

        def user(username_text):
            special_char = "!@#$%^&*()+{}:\"<>?|/'[]~` "
            for char in username_text:
                if char in special_char:
                    tkinter.messagebox.showinfo("Invalid Username", "Username should not contain special characters")
                    return None
            username_text = username_text.lower()
            column_name = "Username"

            if not has_special_char_user(username_text) and len(username_text) > 4:
                if not db["Registration"].find_one({"Username":username_text}):
                    return username_text
                else:
                    tkinter.messagebox.showinfo("Username Taken", "Username is already taken. Please choose another one.")
                    return None
            else:
                tkinter.messagebox.showinfo("Invalid Username", "Username should be more than 4 characters and can only contain digits, underscores and alphabets!")

        def Password(password_text):
            passtren = False
            for i in password_text:
                if i.isupper():
                    passtren = True

            if has_special_char(password_text) and has_digits(password_text) and passtren and len(password_text) >= 7:
                return password_text
            else:
                tkinter.messagebox.showinfo("Invalid Password", "Password should be a minimum of 7 characters, contain special characters, digits, and at least 1 capital letter")
                return None
        def ip_address():
            try:
                return socket.gethostbyname(socket.gethostname())
            except socket.error:
                return None

        validated_name = valid_name(name_text.get())
        validated_username = user(username_text.get())
        validated_password = Password(password_text.get())

        if validated_name and validated_username and validated_password and agree_text.get():
            Error=True
            while Error:
                try:
                    new_document = {
                    "Serial_no": db["Registration"].find_one({}, sort=[("Serial_no", pymongo.DESCENDING)])["Serial_no"]+1,
                    "Timestamp":datetime.now(),
                    "Local_Ip": ip_address(),
                    "Name": validated_name,
                    "Username": validated_username,
                    "Password": validated_password,
                    "Block_status": False,
                    "Useragreement": agree_text.get()
                    }
                    #db["Registration"].insert_one(new_document)
                    Error=False
                except pymongo.errors.DuplicateKeyError:
                    Error = True
            signup_window.destroy()
            tkinter.messagebox.showinfo("Registered!","You have successfully signed up. now you can login")
    b1 = Button(signup_window, text="signup", width=20, command=signupp)
    b1.grid(row=5, column=3)

    b2= Button(signup_window, text="Back", width=20, command=signup_back)
    b2.grid(row=6,column=3)
    signup_window.mainloop()
#----------------X-------------X---------------------X
                 #[CHAT-SCREEN]#
#----------------X-------------X---------------------X
def chat(username_text1):
    global chat_window
    chat_window = tk.Toplevel(window)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    chat_window.geometry(f"{screen_width}x{screen_height}")
    chat_window.title("Inbox")
    l1 = Label(chat_window, text="INBOX", font="times 20")
    l1.pack()

    chat_frame = tk.Frame(chat_window)
    chat_frame.pack(pady=40)

    chat_text = tk.Text(chat_frame, wrap=tk.WORD, state=tk.DISABLED)
    chat_text.pack()

    entry = tk.Entry(chat_frame, width=50)
    entry.pack()
    def logout():
        chat_window.destroy()
        window.deiconify()
    def ip_address():
        try:
            return socket.gethostbyname(socket.gethostname())
        except socket.error:
            return None
    def send_message():
        message = entry.get()
        chat_text.config(state=tk.NORMAL)
        if message!="":
            new_document={
                "Serial_no": db["Chat"].find_one({}, sort=[("Serial_no", pymongo.DESCENDING)])["Serial_no"]+1,
                "Timestamp":datetime.now(),
                "Local_Ip": ip_address(),
                "Sender":username_text1,
                "Message":message}
            db["Chat"].insert_one(new_document)
            time.sleep(1)
        chat_text.config(state=tk.DISABLED) 
        entry.delete(0, tk.END)
    def recieve_message(sender,message):
        chat_text.config(state=tk.NORMAL)
        if message!="":
            chat_text.insert(tk.END, f"{sender}: {message}\n")
        chat_text.config(state=tk.DISABLED) 
        entry.delete(0, tk.END)     


    def check_msg():
        try:
            cursor = mycollection.find({}, fields).sort("Timestamp", pymongo.DESCENDING).limit(5)
            msgs=[]
            for document in cursor:
                msgs.append((document["Sender"],document["Message"]))
            time.sleep(1)
            cursor1 = mycollection.find({}, fields).sort("Timestamp", pymongo.DESCENDING).limit(5)
            msgsnew=[]
            for document in cursor1:
                msgsnew.append((document["Sender"],document["Message"]))
            
            for i in msgs:
                if i in msgsnew:
                    msgsnew.remove(i)
            if msgsnew!=[]:
                for i in msgsnew:
                    recieve_message(i[0],i[1])
        except:
            pass    
                                                 
        finally:
            cursor.close()
    mycollection = db["Chat"]
    fields = {"_id": 1, "Sender": 1, "Message": 1}
    result = mycollection.find({}, fields).sort("Timestamp", pymongo.DESCENDING).limit(5)    
    list_result=list(result)

    for i in range(len(list_result)-1,-1,-1):
        recieve_message(list_result[i]['Sender'],list_result[i]['Message'])
    def chat_thread():
        while True:
            check_msg()
            
    mycollection = db["Chat"]

        
    send_button = tk.Button(chat_frame, text="Send", command=send_message)
    send_button.pack()

    exit_button=Button(chat_frame, text="Logout", command=logout)
    exit_button.pack()
    
    chat_update_thread = threading.Thread(target=chat_thread)
    chat_update_thread.daemon = True  
    chat_update_thread.start()
    
    chat_window.mainloop()
#----------------X------------------X---------------------X
                 #[ADMINCHAT-SCREEN]#
#----------------X------------------X---------------------X    
def adminchat(username_text1):
    global chat_window
    chat_window = tk.Toplevel(window)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    chat_window.geometry(f"{screen_width}x{screen_height}")
    chat_window.title("Inbox")
    l1 = Label(chat_window, text="INBOX", font="times 20")
    l1.pack()

    chat_frame = tk.Frame(chat_window)
    chat_frame.pack(pady=40)

    chat_text = tk.Text(chat_frame, wrap=tk.WORD, state=tk.DISABLED)
    chat_text.pack()

    entry = tk.Entry(chat_frame, width=50)
    entry.pack()
    def logout():
        chat_window.destroy()
        window.deiconify()
    def ip_address():
        try:
            return socket.gethostbyname(socket.gethostname())
        except socket.error:
            return None
    def send_message():
        message = entry.get()
        chat_text.config(state=tk.NORMAL)
        if message!="":
            new_document={
                "Serial_no": db["Chat"].find_one({}, sort=[("Serial_no", pymongo.DESCENDING)])["Serial_no"]+1,
                "Timestamp":datetime.now(),
                "Local_Ip": ip_address(),
                "Sender":username_text1,
                "Message":message}
            db["Chat"].insert_one(new_document)
            time.sleep(1)
        chat_text.config(state=tk.DISABLED) 
        entry.delete(0, tk.END)
    def recieve_message(sender,message):
        chat_text.config(state=tk.NORMAL)
        if message!="":
            chat_text.insert(tk.END, f"{sender}: {message}\n")
        chat_text.config(state=tk.DISABLED) 
        entry.delete(0, tk.END)     


    def check_msg():
        try:
            cursor = mycollection.find({}, fields).sort("Timestamp", pymongo.DESCENDING).limit(5)
            msgs=[]
            for document in cursor:
                msgs.append((document["Sender"],document["Message"]))
            time.sleep(1)
            cursor1 = mycollection.find({}, fields).sort("Timestamp", pymongo.DESCENDING).limit(5)
            msgsnew=[]
            for document in cursor1:
                msgsnew.append((document["Sender"],document["Message"]))
            
            for i in msgs:
                if i in msgsnew:
                    msgsnew.remove(i)
            if msgsnew!=[]:
                for i in msgsnew:
                    recieve_message(i[0],i[1])
        except:
            pass    
                                                 
        finally:
            cursor.close()
    mycollection = db["Chat"]
    fields = {"_id": 1, "Sender": 1, "Message": 1}
    result = mycollection.find({}, fields).sort("Timestamp", pymongo.DESCENDING).limit(5)    
    list_result=list(result)

    for i in range(len(list_result)-1,-1,-1):
        recieve_message(list_result[i]['Sender'],list_result[i]['Message'])
    def chat_thread():
        while True:
            check_msg()

    def control_panel():
        panel_window = tk.Toplevel(chat_window)
        panel_window.geometry("800x650")
        panel_window.title("CONTROL-PANEL")

        l0 = tk.Label(panel_window,text="CONTROL-PANEL",font="times 25")
        l0.grid(row=1,column=1)
        
        labelcol = tk.Label(panel_window,text="\n".join(db.list_collection_names()),font="times 10")
        labelcol.grid(row=3,column=1)
    
        l1 = tk.Label(panel_window,text="Collection name",font="times 10")
        l1.grid(row=2,column=2)
        col_name = StringVar()
        e1 = Entry(panel_window, textvariable=col_name)
        e1.grid(row=3, column=2)

        l2 = tk.Label(panel_window,text="Username",font="times 10")
        l2.grid(row=4,column=2)
        block_unblock = StringVar()
        e2 = Entry(panel_window, textvariable=block_unblock)
        e2.grid(row=5,column=2)

        l3 = tk.Label(panel_window,text="Collection name",font="times 10")
        l3.grid(row=6,column=2)
        delall = StringVar()
        e3 =  Entry(panel_window,textvariable=delall)
        e3.grid(row=7,column=2)

        l4 = tk.Label(panel_window,text="Collection name",font="times 10")
        l4.grid(row=8,column=2)
        collec_name = StringVar()
        e4 = Entry(panel_window,textvariable=collec_name)
        e4.grid(row=9,column=2)

        l5 = tk.Label(panel_window,text="Serial number", font="times 10")
        l5.grid(row=8,column=3)
        serial_no = IntVar()
        e5 =  Entry(panel_window,textvariable=serial_no)
        e5.grid(row=9,column=3)
        
        def allcol():
            labelcol.config(text="\n".join(db.list_collection_names().sort()))
                
        allcol_button=tk.Button(panel_window, text="All Collections", command=allcol)
        allcol_button.grid(row=2,column=1)

        def exitt():
            panel_window.destroy()

        exit_button=tk.Button(panel_window, text="CLOSE", command=exitt)
        exit_button.grid(row=13,column=3)
        
        def createcol():
            try:
                db.create_collection(col_name.get())
                e1.delete(0, tk.END)
            except:
                pass
        create_col=tk.Button(panel_window, text="Create collection", command=createcol)
        create_col.grid(row=3,column=3)
        
        def delcol():
            try:
                db[col_name.get()].drop()
                e1.delete(0, tk.END)
            except:
                pass
            
        del_col=tk.Button(panel_window, text="Delete collection", command=delcol)
        del_col.grid(row=3,column=4)
        
        def alldata():
            def chatwin():
                CHAT_window = tk.Toplevel(panel_window)
                CHAT_window.geometry("300x350")
                CHAT_window.title("CHAT")
                mycollection = db["Chat"]
                all_documents = mycollection.find()
                data = [document for document in all_documents]
                l1=tk.Label(CHAT_window,text=tabulate(data, headers="keys", tablefmt="grid"),font="times 10",justify="left")
                l1.pack()

            def regwin():
                REG_window = tk.Toplevel(panel_window)
                REG_window.geometry("300x350")
                REG_window.title("REGISTRATION")
                mycollection = db["Registration"]
                all_documents = mycollection.find()
                data = [document for document in all_documents]
                l2=tk.Label(REG_window,text=tabulate(data, headers="keys", tablefmt="grid"),font="times 10",justify="left")
                l2.pack()

            def logwin():
                LOGIN_window = tk.Toplevel(panel_window)
                LOGIN_window.geometry("300x350")
                LOGIN_window.title("LOGIN")
                mycollection = db["Login"]
                all_documents = mycollection.find()
                data = [document for document in all_documents]
                l3=tk.Label(LOGIN_window,text=tabulate(data, headers="keys", tablefmt="grid"),font="times 10",justify="left")
                l3.pack()
            chatwin()
            regwin()
            logwin()
        all_data=tk.Button(panel_window, text="ALL DATA", command=alldata)
        all_data.grid(row=12,column=4)

        def block():
            db["Registration"].update_one({"Username":block_unblock.get()},{"$set":{"Block_status":True}})
            e2.delete(0, tk.END)
        block=tk.Button(panel_window, text="Block", command=block)
        block.grid(row=5,column=3)

        def unblock():
            db["Registration"].update_one({"Username":block_unblock.get()},{"$set":{"Block_status":False}})
            e2.delete(0, tk.END)
        unblock=tk.Button(panel_window, text="Unblock", command=unblock)
        unblock.grid(row=5,column=4)

        def dele_all():
            mycollection = db[delall.get()]
            filter = {"Serial_no": {"$gt": 0}}
            mycollection.delete_many(filter)
            e3.delete(0,tk.END)
        del_all=tk.Button(panel_window, text="Delete all", command=dele_all)
        del_all.grid(row=7,column=3)

        def del_one():
            db[collec_name.get()].delete_one({"Serial_no": serial_no.get()})
        del_one_button=tk.Button(panel_window,text="Delete Record",command=del_one)
        del_one_button.grid(row=9,column=4)
        
    mycollection = db["Chat"]

    control_panel_button = tk.Button(chat_frame, text="Control-Panel",command=control_panel)
    control_panel_button.pack()
    
    send_button = tk.Button(chat_frame, text="Send", command=send_message)
    send_button.pack()

    exit_button=Button(chat_frame, text="Logout", command=logout)
    exit_button.pack()
    
    chat_update_thread = threading.Thread(target=chat_thread)
    chat_update_thread.daemon = True  
    chat_update_thread.start()
    
    chat_window.mainloop()    
#----------------X-------------X-----------------X
                 #[MAIN _ BODY]#
#----------------X-------------X-----------------X    
main()
window.mainloop()
