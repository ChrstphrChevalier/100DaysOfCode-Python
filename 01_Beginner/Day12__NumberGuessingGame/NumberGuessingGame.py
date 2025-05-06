import art
import random

print("WELCOME TO")
print(art.logo)

numbers = list(range(1, 101))
easy = 10
hard = 5

print("I'm thinking of a number between 1 and 100.")
choose = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
if choose == 'easy':
    choose = easy
else:
    choose = hard

choice = random.choice(numbers)
win = False
for i in range(choose):
    if i > 0:
        print("Guess again")
    print(f"You have {choose - i} attempts remaining to guess the number")
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        continue
    if guess > choice:
        print("Too high.")
    elif guess < choice:
        print("Too low.")
    else:
        print(f"You got it! The answer was {choice}")
        win = True
        break
if not win:
    print("You've run out of guesses. Refresh the page to run again.")