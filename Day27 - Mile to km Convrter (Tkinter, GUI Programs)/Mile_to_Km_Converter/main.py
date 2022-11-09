from tkinter import *

#function called when calculate button clicked
def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.609
    #use f-string to convert float to string
    km_result_label.config(text=f"{km}")

#window from Tk class
window = Tk()
#Title of window
window.title("Mile to Km Converter")
#setting window size
window.minsize(width=250, height=150)
#adding space around all four edges of screen
window.config(padx=30, pady=30)

#Miles entry box created
miles_input = Entry(width=7)
print(miles_input.get())
miles_input.grid(column=1, row=0)

#initializing label class
is_equal_label = Label(text="is equal to")
#placing label on grid layout
is_equal_label.grid(column=0, row=1)

#label class
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

#label class
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#label class
km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

#Creating calculate button
#When button detects a click event it triggers button_clicked function above
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


#loop which maintains screen display
window.mainloop()