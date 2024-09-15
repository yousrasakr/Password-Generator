from tkinter import *
from PIL import Image, ImageTk
import string
import random

class Password:
    def __init__(self):
        self.s1 = list(string.ascii_uppercase)
        self.s2 = list(string.ascii_lowercase)
        self.s3 = list(string.digits)
        self.s4 = list(string.punctuation)
        self.number_of_chars = 0

    # Shuffling characters
    def shuffling(self): 
        random.shuffle(self.s1)
        random.shuffle(self.s2)
        random.shuffle(self.s3)
        random.shuffle(self.s4)

    # Generate a strong password
    def evaluate_pass(self):
        self.shuffling()
        part1 = round(self.number_of_chars * (30 / 100))
        part2 = round(self.number_of_chars * (20 / 100))
        strong_password = []

        for i in range(part1):
            strong_password.append(self.s1[i])
            strong_password.append(self.s2[i])

        for i in range(part2):
            strong_password.append(self.s3[i])
            strong_password.append(self.s4[i])

        random.shuffle(strong_password)
        self.get_pass(strong_password)

    # Display the password
    def get_pass(self, strong_password):  
        strong_password = "".join(strong_password)
        outputtxt.config(state=NORMAL)
        outputtxt.delete(1.0, END)  # Clear the output box
        outputtxt.insert(END, f"Your strong password is:\n{strong_password}")
        outputtxt.config(state=DISABLED)

# GUI setup
myframe = Tk()
passw = Password()

# GUI functions
def evaluate_pass_gui():
    try:
        passw.number_of_chars = int(inputtxt.get())
        if passw.number_of_chars < 6:
            outputtxt.config(state=NORMAL)
            outputtxt.delete(1.0, END)
            outputtxt.insert(END, "You need at least 6 characters!")
            outputtxt.config(state=DISABLED)
        else:
            passw.evaluate_pass()
    except ValueError:
        outputtxt.config(state=NORMAL)
        outputtxt.delete(1.0, END)
        outputtxt.insert(END, "Please enter a valid number!")
        outputtxt.config(state=DISABLED)

# Load background image
img = Image.open("bground.jpg")
background_image = ImageTk.PhotoImage(img)

# Create a label widget to hold the image
background_label = Label(myframe, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create label for the title
Label1 = Label(myframe, text="Strong Password Generator", bg="#283593", fg="white", pady=10, padx=10)
Label1.config(font=("Helvetica", 18, "bold"))
Label1.pack(pady=20)

# Create label for description
Label2 = Label(myframe, text="Fortify your accounts with unbeatable passwords. Generate now!", anchor=W, bg="#3f51b5", fg="white")
Label2.config(font=("Helvetica", 10))
Label2.pack(pady=5)

# Create label for user input
Label3 = Label(myframe, text="Enter the number of characters you want:", pady=15, bg="#283593", fg="white")
Label3.config(font=("Helvetica", 12))
Label3.pack()

# Create an entry widget for user input
inputtxt = Entry(myframe, width=30, font=("Helvetica", 14), bd=2, relief="groove")
inputtxt.pack(pady=10)

# Create a button to generate the password
b1 = Button(myframe, text="Generate", height=2, width=15, command=evaluate_pass_gui, bg="#3949ab", fg="white", bd=3, relief="raised")
b1.config(font=("Helvetica", 12, "bold"))
b1.pack(pady=30)

# Create a text widget to display the output
outputtxt = Text(myframe, height=8, width=40, font=("Helvetica", 12), bg="#e8eaf6", fg="black", bd=2, relief="sunken", wrap=WORD)
outputtxt.pack(pady=10)
outputtxt.config(state=DISABLED)

# GUI setup
myframe.title("STRONG PASSWORD GENERATOR")
myframe.geometry("600x600")
myframe.resizable(False, False)  # Make the window size fixed
myframe.mainloop()
