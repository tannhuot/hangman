import random
# import hangman_art
# import hangman_art as art
from hangman_art import *
import hangman_words

score = 6
word = ["Apple", "Book"] #hangman_words.word_list
random_word = ""
guess_word = []
guessed_character = []
user_input = ""

print(logo)


def ask_user_confirm(message):
    while True:
        user_input = input(message)
        if user_input == "y" or user_input == "n":
            break
    return user_input


def showScoreAndStage(message: str, score: int, stage: str):
    if message != "":
        print(message)
    print(f"Your score is {score}")
    print(stage)


user_input = ask_user_confirm("Are you ready to play? [y/n]: ")

while user_input == "y":
    showScoreAndStage("", score, stages[score])
    print("Please guess the word below:")
    random_word = random.choice(word)
    for char in random_word:
        guess_word.append("_")

    print("".join(guess_word))

    while score > 0:
        while True:
            user_guess = input("Enter your guessing character: ")
            if user_guess in guessed_character:
                print("You already guessed this character. Please try again.")
            elif len(user_guess) != 1:
                print("You can only enter 1 character.")
            else:
                break

        guessed_character.append(user_guess)

        if user_guess in random_word:
            showScoreAndStage("You're correct!", score, stages[score])

            # for idx in range(len(random_word)):
            #     if user_guess == random_word[idx]:
            #         guess_word[idx] = user_guess

            idx = random_word.find(user_guess)
            while idx > -1:
                guess_word[idx] = user_guess
                idx = random_word.find(user_guess, idx + 1)

            print("".join(guess_word))

            if str(guess_word).find("_") == -1:
                print("Congratulations! You win....")
                print(win_logo)
                break
        else:
            score -= 1
            showScoreAndStage("Your answer is incorrect. Please try again...", score, stages[score])
            if score == 0:
                print(f"The word is: {random_word}\nGame Over....")
                break

    user_input = ask_user_confirm("Do you want to play again? [y/n]: ")
print("Good bye...")
