import random


class StartQuiz:

    def __init__(self, questions_asked):
        self.score = 0
        self.num_of_questions = questions_asked
        self.question_num = []

    def ask_question(self, q_list):
        q_num = random.randint(0, 39)
        while q_num in self.question_num:
            self.question = random.randint(0, 39)
        self.question_num.append(q_num)

        self.question = q_list[q_num]
        self.q_text = self.question.text
        self.q_answer = self.question.answer

        self.guess = input(f"{self.q_text}. Type True/False: ")

    def is_answer_correct(self):
        if self.q_answer == "True":
            if self.guess == "True":
                return True
            elif self.guess == "False":
                return False
            else:
                print("Please type in correctly.")
                self.ask_question()
                self.is_answer_correct()
        else:
            if self.guess == "True":
                return False
            elif self.guess == "False":
                return True
            else:
                print("Please type in correctly.")
                self.ask_question()
                self.is_answer_correct()

    def quiz_score(self):
        if self.is_answer_correct():
            self.score += 1

        self.num_of_questions += 1

        return self.score
