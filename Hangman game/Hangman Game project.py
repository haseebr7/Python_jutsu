import random
import hangman_words
import hangman_art


lives = 6

logo = hangman_art.logo
print(logo)

chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************You have {lives} LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()


    display = ""
    if guess in correct_letters:
        print(f'letter "{guess}" you already guessed.')
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        print(f'''You guessed letter "{guess}", that's not in the word. You lose a life''')
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print(f"You failed to guess the word \n [{chosen_word}]")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
