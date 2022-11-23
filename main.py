from data import question_data
from question_model import Question
from quiz_brain import StartQuiz

questions_asked = 1
quizbrain = StartQuiz(questions_asked)
question_bank = []
end_of_quiz = False

for question in question_data:
    q_text = question['text']
    q_answer = question['answer']

    question = Question(q_text, q_answer)
    question_bank.append(question)

while not end_of_quiz and questions_asked < 6:
    quizbrain.ask_question(question_bank)
    quiz_score = quizbrain.quiz_score()
    questions_asked += 1


print(f"Your score is {quiz_score}/5")
