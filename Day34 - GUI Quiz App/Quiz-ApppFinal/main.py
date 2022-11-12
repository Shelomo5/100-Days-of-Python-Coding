from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # Question object created from question class which has self.text and self.answer attributes
    new_question = Question(question_text, question_answer)
    # Append question objects to list
    question_bank.append(new_question)

# pass list to the QuizBrain class when instantiating object
quiz = QuizBrain(question_bank)
# object created by QuizInterface class
# pass in quiz when we create quiz_ui
quiz_ui = QuizInterface(quiz)

# while loop needs to be commented out for GUI to work properly
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
