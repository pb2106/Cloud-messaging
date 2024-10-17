import tkinter as tk

def destroy():
    window.destroy()

window = tk.Tk()
window.title("Buttons with Font Size")

# Specify the font size using the `font` option
button1 = tk.Button(window, text="Button 1", font=("Helvetica", 12), command=lambda: print("Button 1 clicked"))
button1.pack(pady=10)

button2 = tk.Button(window, text="Button 2", font=("Arial", 14, "bold"), command=lambda: print("Button 2 clicked"))
button2.pack(pady=10)

button3 = tk.Button(window, text="Exit", font=("Times", 16, "italic"), command=destroy)
button3.pack(pady=10)

window.mainloop()
