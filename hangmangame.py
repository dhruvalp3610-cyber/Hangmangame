import random

words = ["python", "apple", "banana", "school", "computer"]

while True:

    word = random.choice(words)
    guessed_word = ["_"] * len(word)

    guessed_letters = []
    wrong_guesses = 0
    max_guesses = 6

    score = 0
    hint_used = False

    print("\n===== HANGMAN GAME =====")
    print("Type 'hint' to reveal one letter (only once).")

    while wrong_guesses < max_guesses and "_" in guessed_word:

        print("\nWord:", " ".join(guessed_word))
        print("Guessed Letters:", " ".join(guessed_letters))
        print("Score:", score)
        print("Incorrect Guesses Left:", max_guesses - wrong_guesses)

        guess = input("Enter a letter: ").lower().strip()

        # Hint Feature
        if guess == "hint":

            if hint_used:
                print("Hint already used!")
                continue

            for i in range(len(word)):
                if guessed_word[i] == "_":
                    guessed_word[i] = word[i]
                    guessed_letters.append(word[i])
                    hint_used = True
                    score -= 2
                    print(f"Hint Used! Letter revealed: {word[i]}")
                    break

            continue

        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet.")
            continue

        # Already guessed
        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue

        guessed_letters.append(guess)

        # Correct Guess
        if guess in word:
            print("Correct!")

            count = 0

            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
                    count += 1

            score += count * 2

        # Wrong Guess
        else:
            print("Wrong!")
            wrong_guesses += 1
            score -= 1

    # Final Result
    if "_" not in guessed_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        print("Final Score:", score)

    else:
        print("\n💀 Game Over!")
        print("The word was:", word)
        print("Final Score:", score)

    play_again = input("\nPlay Again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank you for playing!")
        break