
#class used to bring up question and ask user to answer the question
#asking the questions, checking if answer was correct, checking if at end of quiz
class QuizBrain:

    def __init__(self, q_list):
        #every time we create a new quiz brain object from this class it has attribute set to 0
        # keeps track of which question the user is on
        self.question_number = 0
        self.score = 0
        #question_bank from main passed into as q_list, a list of of Question objects created in
        #main as question_bank and stored in as self.question_list
        self.question_list = q_list


    def still_has_questions(self):
        #when you return expression if less than will return True if not less than it will return false
        return self.question_number < len(self.question_list)

    def next_question(self):
        #one question object pulled out of the list and assigned to current_question
        #From Question class each current_question object in list has a text and answer attribute
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        #current_question.text is is a Question class object
        user_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    #passing in user_answer, current_question.answer as parameters
    def check_answer(self, user_answer, correct_answer ):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/ {self.question_number}")
        print("\n")
