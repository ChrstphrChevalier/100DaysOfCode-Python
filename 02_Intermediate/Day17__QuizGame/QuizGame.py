from Q_model import Question
from Q_data import q_data
from Q_brain import QuizBrain

question_bank = []
for item in q_data:
    question_bank.append(Question(item['text'], item['answer']))

QuizGame = QuizBrain(question_bank)
while QuizGame.still_has_question():
    QuizGame.next_question()
    QuizGame.check_answer()
    print("\n" * 2)