#Task 1:Hangman Game
import random

def choose_word():
    # List of words to choose from
    words = ['python', 'hangman', 'programming', 'development', 'challenge']
    return random.choice(words)

def display_word(word, guesses):
    return ' '.join([letter if letter in guesses else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Maximum number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print(f"Guess the word: {display_word(word, guessed_letters)}")

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} attempts left.")

        current_display = display_word(word, guessed_letters)
        print(f"Word: {current_display}")

        if '_' not in current_display:
            print(f"Congratulations! You've guessed the word '{word}'.")
            break
    else:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    hangman()



#output:
'''
Welcome to Hangman!
Guess the word: _ _ _ _ _ _ _ _ _
Guess a letter: a
Good guess!
Word: _ _ a _ _ _ _ _ _
Guess a letter: h
Good guess!
Word: _ h a _ _ _ _ _ _
Guess a letter: l
Good guess!
Word: _ h a l l _ _ _ _
Guess a letter: e
Good guess!
Word: _ h a l l e _ _ e
Guess a letter: c
Good guess!
Word: c h a l l e _ _ e
Guess a letter: n
Good guess!
Word: c h a l l e n _ e
Guess a letter: g
Good guess!
Word: c h a l l e n g e
Congratulations! You've guessed the word 'challenge'. '''
