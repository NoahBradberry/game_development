import tkinter as tk

def say_hi():
    button.config(text = "Unclick Me")
    unclick_button.pack()
def say_bye():
    label.config(text = "Hello TKinter")
    unclick_button.pack_forget()
#Create the main window
root = tk.Tk()
root.title("My First TKinter Project")
root.geometry("400x300")

label = tk.Label(root, text = "Hello, TKinter")
label.pack()

button = tk.Button(root, text = "Click Me!", command = say_hi, bg = "green")
button.pack()

unclick_button = tk.Button(root, text = "Unclick Button", command = say_bye)


#Runs the Program above
root.mainloop()