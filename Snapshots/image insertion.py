# Import module 
import tkinter as tk
from tkinter import *
# Create object 
root = tk.Tk() 
def fil():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}")

    bg = PhotoImage(file = "reg_login.png") 

    # Show image using label 
    label1 = Label( root, image = bg) 
    label1.place(x = 0, y = 0)
    root.mainloop()
"""
label2 = Label( root, text = "Welcome") 
label2.pack(pady = 50) 

# Create Frame 
frame1 = Frame(root) 
frame1.pack(pady = 20 ) 

# Add buttons 
button1 = Button(frame1,text="Exit") 
button1.pack(pady=20) 

button2 = Button( frame1, text = "Start") 
button2.pack(pady = 20) 

button3 = Button( frame1, text = "Reset") 
button3.pack(pady = 20) 
"""
# Execute tkinter
fil()

