class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.answer = ""
        self.current_score = 0
        self.q_list = q_list

    def still_has_question(self):
        if self.q_number < len(self.q_list):
            return True
        print("The End. You've completed the Quiz. Goodbye :)")
        return False

    
    def next_question(self):
        Q = self.q_list[self.q_number]
        self.q_number += 1
        self.answer = input(f"Q.{self.q_number}: {Q.q_text}. (True/False)?: ")

    def check_answer(self):
        if self.answer == self.q_list[self.q_number].q_answer:
            print("You got it right!")
            self.current_score += 1
        else:
            print("Don't be discouraged!")
        print(f"The correct answer was: {self.q_list[self.q_number].q_answer}")
        print(f"Your current score is: {self.current_score}/{self.q_number}.")