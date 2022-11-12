from tkinter import *
# import QuizBrain class
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

# class responsible for displaying quiz items on the screen
class QuizInterface:
    # init is called whenever we create a new object from this class
    # quiz_brain (QuizBrain data type) object passed in as a parameter when class is initialized
    def __init__(self, quiz_brain: QuizBrain):
        # quiz_brain received when we initialize new interface
        self.quiz = quiz_brain
        # adding self to window object(from Tk class) to make it a property of this class
        self.window = Tk()
        # setting title of window
        self.window.title("Quizzler")
        # adding padding and background color
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        # Creating canvas, useful bc it allows us to layer a lot of things on top of it
        self.canvas = Canvas(width=300, height=250, bg="white")
        # creating canvas text item
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 290, # ensures text goes on separate lines and doesn't leave border
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        # places canvas in row 1 and spans both columns
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        # creating true and false buttons with command to functions when button is pressed
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command = self.button_true)
        self.true_button.grid(row=2, column=0)
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command = self.button_false)
        self.false_button.grid(row=2, column=1)

        # score label
        self.score_label = Label(text=f"score: ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # call method to fetch the first question when QuizInterface is initialized
        self.get_next_question()

        # constantly runs to check if GUI needs to be updated
        self.window.mainloop()

    # will call next_question from the quiz_brain class
    def get_next_question(self):
        # reset background to white in next question
        self.canvas.config(bg="white")
        # QuizBrain method used to check there's a next question
        if self.quiz.still_has_questions():
            # change score passing in QuizBrain object quiz with score attribute
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # call next question method on quiz to get question text that it received
            q_text = self.quiz.next_question()
            # update question_text item in canvas to q_text
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # change canvas text to notify user quiz is over
            self.canvas.itemconfig(self.question_text, text="There are no more question, the quiz is over")
            # disabled state means button can't be pressed
            self.true_button.config(state="disable")
            # disabled state means button can't be pressed
            self.false_button.config(state="disable")
    # if true button pressed call check_answer method from quiz_brain class
    # to check if True was the right answer
    def button_true(self):
        # "True" is the button user clicks
        # is_right stores if check_answer returns True or False
        is_right = self.quiz.check_answer("True")
        # is_right passed to function give_feedback
        self.give_feedback(is_right)

    def button_false(self):
        # "False" is the button user clicks
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        # if the output of check answer() is true then change color to green, otherwise red
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # delay 1000 ms before calling get_next_question function to switch question
        self.window.after(1000, self.get_next_question)
