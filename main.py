from data import question_data
from question_model import Question
from quiz_brain import BrainQuiz
question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

 
quiz = BrainQuiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz \nYour final score: {quiz.score}/{quiz.question_number}")