import random
words = ["python", "coding", "computer", "school", "display"]
# Randomly choose a word
secret_word = random.choice(words)
display_word = ["_"] * len(secret_word)
# Store guessed letters
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=================================")
print("      WELCOME TO HANGMAN")
print("=================================")

while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Guessed Letters:", ", ".join(guessed_letters))
    print("Attempts Left:", max_wrong_guesses - wrong_guesses)
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)
    if guess in secret_word:
        print("Correct Guess!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong Guess!")
print("\n=================================")
if "_" not in display_word:
    print("Congratulations! You Won 🎉")
    print("The word was:", secret_word)
else:
    print("Game Over 😢")
    print("The correct word was:", secret_word)
print("=================================")