import random
import hangman_art
import hangman_words

word_chosen = random.choice(hangman_words.word_list)
hide_word = ["_"] * len(word_chosen)

level = hangman_art.stages
lives = 6

print(hangman_art.logo)
print(word_chosen)

while lives > 0:
    guess = input("Guess a letter: ").lower()
    found = False

    for index, letter in enumerate(word_chosen):
        if letter == guess:
            hide_word[index] = guess
            found = True

    if not found:
        print("Wrong")
        lives -= 1
    else:
        print("Right")

    print(level[lives])
    print("".join(hide_word))
    
    if lives > 0 and "_" in hide_word:
        print(f"You have {lives} lives left")
    if "_" not in hide_word:
        print("Congratulation, You Win :)")

if lives == 0:
    print("Game Over, try again")