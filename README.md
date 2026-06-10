# 🎮 Hangman Game in Python

## 📌 Project Overview

This is a simple command-line Hangman Game developed using Python. The player has to guess the hidden word one letter at a time before running out of attempts.

The game includes:

* Random word selection
* Score tracking system
* Hint feature
* Input validation
* Replay option

---

## 🚀 Features

### ✅ Random Word Selection

A random word is selected from a predefined list every time a new game starts.

### ✅ Score System

* Correct letter: **+2 points**
* Wrong letter: **-1 point**
* Hint usage: **-2 points**

### ✅ Hint Feature

* Type `hint` to reveal one hidden letter.
* Can only be used **once per game**.

### ✅ Input Validation

The game checks that:

* Only one character is entered.
* Input contains only alphabets.
* Previously guessed letters cannot be entered again.

### ✅ Replay Functionality

After each game, the player can choose to play again without restarting the program.

---

## 🛠️ Technologies Used

* Python 3
* Random Module

---

## 📂 Project Structure

```
Hangman-Game/
│
├── hangmangame.py
└── README.md
```

---

## ▶️ How to Run

### Step 1: Install Python

Download and install Python from:
https://www.python.org/downloads/

### Step 2: Open Terminal or Command Prompt

Navigate to the project folder:

```bash
cd Hangman-Game
```

### Step 3: Run the Program

```bash
python hangmangame.py
```

---

## 🎯 Game Rules

1. A random word is chosen by the system.
2. The player guesses one letter at a time.
3. Maximum incorrect guesses allowed: **6**
4. Type `hint` to reveal one letter.
5. Guess the complete word before running out of attempts.
6. Final score is displayed at the end of the game.

---

## 📸 Sample Output

```
===== HANGMAN GAME =====
Type 'hint' to reveal one letter (only once).

Word: _ _ _ _ _ _
Guessed Letters:
Score: 0
Incorrect Guesses Left: 6

Enter a letter: p
Correct!

Word: p _ _ _ _ _
Score: 2
```

---

## 🔮 Future Enhancements

* Multiple difficulty levels
* Larger word database
* Categories (Animals, Fruits, Countries, etc.)
* ASCII Hangman Drawing
* High Score System
* Timer-based Challenges
* GUI Version using Tkinter or PyQt

---

## 👨‍💻 Author

Developed as a Python Mini Project for learning:

* Loops
* Conditional Statements
* Lists
* String Manipulation
* User Input Handling
* Basic Game Development

---

## 📜 License

This project is free to use for educational and learning purposes.
