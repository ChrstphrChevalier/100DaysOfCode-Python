import art
import random
import stars

print("WELCOME TO")
print(art.logo)

game = True
final_score = 0
more = ""

which_stars = dict(zip(['A', 'B'], random.sample(stars.stars, 2)))

def switch(more, which_stars):
    new_ws = which_stars
    old_A = new_ws['A']
    old_B = new_ws['B']
    if more == 'A':
        while True:
            new_ws['B'] = random.choice(stars.stars)
            if new_ws['B']['name'] != old_B['name'] and new_ws['B']['name'] != old_A['name']:
                return new_ws
    else:
        new_ws['A'] = new_ws['B']
        while True:
            new_ws['B'] = random.choice(stars.stars)
            if new_ws['B']['name'] != old_B['name'] and new_ws['B']['name'] != old_A['name']:
                return new_ws

while game:
    print(f"Compare A: {which_stars['A']['name']}, a {which_stars['A']['description']}, from {which_stars['A']['country']}")
    print(art.vs)
    print(f"Against B: {which_stars['B']['name']}, a {which_stars['B']['description']}, from {which_stars['B']['country']}")
    if which_stars['A']['follower_count'] > which_stars['B']['follower_count']:
        more = 'A'
    else:
        more = 'B'
    choice = input("Who has more followers? Type 'A' or 'B : ").upper()
    print("\n" * 10)
    if (choice != 'A' and choice != 'B') or choice != more:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {final_score}")
        print("\n" * 5)
        game = False
    else:
        final_score += 1
        if final_score > 0:
            print(art.logo)
        print(f"You're right! Current_score: {final_score}")
        which_stars = switch(more, which_stars)