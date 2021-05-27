import random
import os
import time
from logo import stages, logo
from words import word_list

chosen_word = random.choice(word_list)
current_guess = ['_'] * len(chosen_word)
for i in range(int(len(chosen_word)/2)):
    easy = random.randint(0, len(chosen_word))
    current_guess[easy] = chosen_word[easy]
game = False
lives = 6
while not game:
    print(logo)
    print(stages[lives])
    print(current_guess)
    char = input("whats\' your guess ? ")
    if char in chosen_word:
        print("your guess was right ")
        for i in range(len(chosen_word)):
            if chosen_word[i] == char and current_guess[i] == '_':
                current_guess[i] = char
                break

    else:
        lives -= 1
        print("you guessed the wrong letter ")

    if lives == 0:
        game = True
        print(stages[0])
        print("you loose ")
        print(f"the word was {chosen_word}")

    elif "_" not in current_guess:
        game = True
        print(current_guess)
        print("you won")
    time.sleep(1)
    os.system("clear")