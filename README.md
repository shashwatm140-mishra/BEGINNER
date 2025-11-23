# SHASHWAT MISHRA

# 25BCE10515



🎯 Guess the Number Game
Overview of the Project 

This project implements a classic "Guess the Number" game, built as a console application using Python. The objective is for the user to guess a secret random number chosen by the computer within a defined range and number of chances. The game features three distinct difficulty levels to provide a varying challenge.
✨ Features 

The Guess the Number Game includes the following key features:

Three Difficulty Levels: The game offers Level 1 (range 1-5, 2 chances), Level 2 (range 1-10, 3 chances), and Level 3 (range 1-20, 5 chances).

Interactive Menu: A main menu allows the user to select the desired difficulty level or exit the game.

Random Number Generation: A new secret number is randomly generated for each game session.

Win/Loss Feedback: Clear messages inform the user whether they won or lost. In case of a loss, the correct number chosen by the computer is revealed.

Continuous Play: Users can play multiple rounds without restarting the application.
 Technologies/Tools Used:
Python 3.x The core programming language for the application logic.
random moduleUsed for generating the secret integer number within the specified range.
Console/TerminalUsed for all input and output (I/O).
⚙️ Steps to Install & Run the Project 

Prerequisites: Ensure you have Python 3 installed on your system.

Clone the Repository: Download or clone the project files (specifically main.py) to your local machine.

Open Terminal/Command Prompt: Navigate to the directory where you saved the main.py file.
Play the Game: Follow the on-screen instructions to select a level (1, 2, or 3) and enter your guesses. Select 4 to exit.
🧪 Instructions for Testing 

The game can be tested manually by verifying the following scenarios:

Select all three levels (1, 2, and 3) to ensure the correct number range and chance limits are enforced as per the rules.

Test the winning scenario by guessing the correct number before running out of chances. The game should break the loop and display "You Won!!!".

Test the losing scenario by purposely guessing incorrect numbers until the chances run out. The game should reveal the "Computer chose: [number]".

Test the exit option (4) from the main menu.

Test an invalid menu choice (e.g., entering 5) to verify the prompt "GO TO MAIN MENU?[y/n]:" works correctly.

Screenshots:
<img width="890" height="411" alt="Screenshot 2025-11-24 000806" src="https://github.com/user-attachments/assets/56238fdf-c009-4e2c-9f4e-07c1d047a88d" />
<img width="880" height="432" alt="Screenshot 2025-11-24 000849" src="https://github.com/user-attachments/assets/b9948b8c-eb0d-473c-9831-3bc07f66734c" />
<img width="867" height="589" alt="Screenshot 2025-11-24 000904" src="https://github.com/user-attachments/assets/6d14bb7e-c4f2-41ea-a419-75dde2d1a635" />
<img width="881" height="104" alt="Screenshot 2025-11-24 000921" src="https://github.com/user-attachments/assets/9b10473b-bb40-4f6b-b21d-d1fa54bd859d" />


