
#Question class object with answer and text attributes
#The attribute values of each object are passed in as arguments when calling Question()
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

# new_q = Question("sdfgh", "False")
# print(new_q.text)