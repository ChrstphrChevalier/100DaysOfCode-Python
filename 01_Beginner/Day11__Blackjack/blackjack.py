import art
import random
import message


restart = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if restart == 'n':
    exit()

print(" WELCOME TO")
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def blackjack():
    print(f"    Your hand: {player}, final score: {current_score}")
    print(f"    Computer's hand: {computer}, final score: {computer_score}")
    print("🚀🚀 !! BLACKJACK !! 🚀🚀")

def show_result():
    print(f"    Your final hand: {player}, final score: {current_score}")
    print(f"    Computer's final hand: {computer}, final score: {computer_score}")

    if computer_score > 21 or (computer_score < current_score and current_score < 21):
        print(random.choice(message.win))
    elif computer_score == current_score:
        print(random.choice(message.draw))
    else:
        print(random.choice(message.lose))

def handle_computer():
    global computer, computer_score
    while True:
        computer.append(random.choice(cards))
        computer_score = sum(10 if card in ['J', 'Q', 'K'] else card for card in computer)
        if computer_score == 21 and len(computer) == 2:
            blackjack()
            return
        if computer_score > 21 and 11 in computer:
            computer[computer.index(11)] = 1
            computer_score -= 10
        if computer_score > 16:
            break
    show_result()

def handle_player():
    global player, current_score
    while True:
        if current_score == 21 and len(player) == 2:
            blackjack()
            return

        if current_score > 21 and 11 in player:
            player[player.index(11)] = 1
            current_score -= 10

        if current_score > 21:
            show_result()
            return
        else:
            print(f"    Your cards: {player}, current score: {current_score}")
            print(f"    Computer first card: {computer[0]}")
            while True:
                more_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if more_card == 'y':
                    player.append(random.choice(cards))
                    current_score = sum(10 if card in ['J', 'Q', 'K'] else card for card in player)
                    break
                elif more_card == 'n':
                    handle_computer()
                    return
                else:
                    print(" -> Invalid input, try again")

game = True
while game:
    player = random.sample(cards, 2)
    computer = random.sample(cards, 1)
    current_score = sum(10 if card in ['J', 'Q', 'K'] else card for card in player)
    computer_score = computer[0]
    handle_player()
    while True:
        restart = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if restart == 'y':
            break
        elif restart == 'n':
            game = False
            print(random.choice(message.goodbye))
            break
        else:
            print(" -> Invalid input, try again")