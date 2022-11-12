from tkinter import *
import requests


def get_quote():
    # get data from endpoint which is a URL and store it in a response variable
    response = requests.get(url="https://api.kanye.rest")
    # exception will be raised if status code isn't 200 meaning our request wasn't successful
    response.raise_for_status()

    # retrieving json data
    data = response.json()
    quote = data["quote"]
    # configures text of quote_text item to display quote
    canvas.itemconfig(quote_text, text=quote)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()