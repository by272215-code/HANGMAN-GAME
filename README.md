# 🎮 Hangman Game

## Introduction

Hangman Game is a simple command-line word guessing game developed using Python. This project was created as **Task 1** for the **CodeAlpha Python Programming Internship**.

The objective of the game is to guess a hidden word by entering one letter at a time. The player is given a limited number of incorrect attempts. If the player successfully guesses all the letters before running out of attempts, they win the game. Otherwise, the game ends and the correct word is revealed.

This project demonstrates the use of Python fundamentals such as loops, conditional statements, lists, strings, user input handling, and the random module.



## Project Objectives

The main objectives of this project are:

* To understand the basics of game development using Python.
* To practice problem-solving and logical thinking.
* To work with loops and conditional statements.
* To learn how to manage user input and validate data.
* To gain hands-on experience with Python programming concepts.



## Features

✅ Random word selection from a predefined list

✅ Letter-by-letter word guessing

✅ Tracks all previously guessed letters

✅ Prevents duplicate guesses

✅ Input validation for better user experience

✅ Limited number of incorrect attempts

✅ Displays win and lose messages

✅ Beginner-friendly and easy-to-read code



## Technologies Used

* Python 3
* Random Module


## How the Game Works

1. The program randomly selects a word from a predefined list.
2. The selected word is hidden using underscores (_).
3. The player enters one letter at a time.
4. If the guessed letter exists in the word, it is revealed in the correct position.
5. If the guessed letter is incorrect, one attempt is deducted.
6. The game continues until:

   * The player guesses the complete word, or
   * The player runs out of attempts.
7. The final result is displayed.



## Sample Output

=================================
      WELCOME TO HANGMAN
=================================

Word: _ _ _ _ _ _
Guessed Letters: 
Attempts Left: 6
Enter a letter: s
Correct Guess!

Word: s _ _ _ _ _
Guessed Letters: s
Attempts Left: 6
Enter a letter: c
Correct Guess!

Word: s c _ _ _ _
Guessed Letters: s, c
Attempts Left: 6
Enter a letter: h
Correct Guess!

Word: s c h _ _ _
Guessed Letters: s, c, h
Attempts Left: 6
Enter a letter: o
Correct Guess!

Word: s c h o o _
Guessed Letters: s, c, h, o
Attempts Left: 6
Enter a letter: o
You already guessed this letter.

Word: s c h o o _
Guessed Letters: s, c, h, o
Attempts Left: 6
Enter a letter: l
Correct Guess!

=================================
Congratulations! You Won 🎉
The word was: school
=================================

## Learning Outcomes

By completing this project, I learned:

* Python programming fundamentals
* Working with lists and strings
* Using loops effectively
* Implementing conditional logic
* Handling user input
* Generating random selections
* Building simple interactive console applications


## Future Improvements

Some features that can be added in future versions:

* Multiple difficulty levels
* Larger word database
* Score tracking system
* Graphical User Interface (GUI)
* Hint system
* Multiplayer mode


## Internship Information

**Internship Provider:** CodeAlpha

**Domain:** Python Programming

**Task:** Task 1 - Hangman Game

This project was successfully completed as part of the CodeAlpha Python Programming Internship program.

## Author

**Bittu Kumar**

Thank you for visiting this repository. Feedback and suggestions are always welcome.
