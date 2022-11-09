from tkinter import *

#function called when button clicked
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text= new_text)

#window from Tk class
window = Tk()
#Title of window
window.title("Gui Program")
#setting window size
window.minsize(width=500, height=300)
#adding space around all four edges of screen
window.config(padx=20, pady=20)

#initializing label class
my_label = Label(text='I am a label', font=("Arial", 24, "bold"))
#changing label text
my_label.config(text="New Text")
#placing label on grid layout
my_label.grid(column=0, row=0)
#place padding around widgget
my_label.config(padx=50,pady=50)

#Creating a button
#When button detects a click event it triggers function above
button = Button(text="Click Me", command=button_clicked)
#method places button in the center of the screen
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

#Insert entry box
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

#loop which maintains screen display
window.mainloop()