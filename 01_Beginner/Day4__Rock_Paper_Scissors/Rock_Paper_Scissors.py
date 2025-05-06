import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_choice = [Rock, Paper, Scissors]

choose = input("What do you choose ? 0 for Rock, 1 for Paper, 2 for Scissors.\n")
choice = int(choose)
if choice == game_choice.index(Rock)\
    or choice == game_choice.index(Paper)\
    or choice == game_choice.index(Scissors):
    print(game_choice[choice])
else:
    print("I don't want to play with you anymore.")
    exit()

random_choose = random.randint(0, 2)
print("Computer Chose:")
if random_choose == game_choice.index(Rock)\
    or random_choose == game_choice.index(Paper)\
    or random_choose == game_choice.index(Scissors):
    print(game_choice[random_choose])

if choice == random_choose:
    print("Equality")
elif choice == 0 and random_choose == 2\
    or choice == 1 and random_choose == 0\
    or choice == 2 and random_choose == 1:
    print("You Win :)")
else:
    print("You Lose :(")