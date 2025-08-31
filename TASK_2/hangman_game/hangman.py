import random

# Step 1: Word Selection
words = ["python", "hangman", "programming", "computer", "developer", "banana", "apple"]
word = random.choice(words).lower()
word_letters = set(word)   # unique letters in the word
guessed_letters = set()    # letters guessed by user
incorrect_guesses = 0
max_attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word before the man is hanged!")

# Function to display current progress
def display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Step 7: Game Loop
while incorrect_guesses < max_attempts and len(word_letters) > 0:
    print("\nWord:", display_word())
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print(f"Attempts left: {max_attempts - incorrect_guesses}")

    # Step 4: User Input
    guess = input("Guess a letter: ").lower()

    # Step 5: Check Guess
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
    elif guess in word_letters:
        guessed_letters.add(guess)
        word_letters.remove(guess)
        print("✅ Good guess!")
    else:
        guessed_letters.add(guess)
        incorrect_guesses += 1
        print("❌ Wrong guess!")

# Step 6: Win/Loss Conditions
if len(word_letters) == 0:
    print(f"\n🎉 Congratulations! You guessed the word: {word}")
else:
    print(f"\n💀 You lost! The word was: {word}")
