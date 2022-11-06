from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
#question_model is a class which creates question objects with two attributes
#QuizBrain is a class asking the questions, checking if answer was correct, checking if at end of quiz
#main we created a list of question objects

# creating a list of question objects which have two attributes text and answer
question_bank = []
for question in question_data:
    question_object = Question(question["question"], question["correct_answer"])
    question_bank.append(question_object)

#initialize QuiBrain object
quiz = QuizBrain(question_bank)


while quiz.still_has_questions(): #if quiz still has questions remaining:
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/ {quiz.question_number}")
