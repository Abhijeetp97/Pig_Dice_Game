# Pig Dice Game

## Overview

This repository contains two versions of the Pig Dice Game:
1. **Pig_Dice_game.py** – The original implementation of the game.
2. **Pig_Dice_game_enhanced.py** – An enhanced version with improved readability, robust input validation, clearer instructions (with example inputs), and better error handling.

Both versions allow players to take turns rolling a die to accumulate points while following the game rules (losing points on a roll of 1 or resetting the score on two consecutive 6s). The enhanced version ensures a smoother user experience by guiding the player when invalid inputs are provided.

## Features

- **Simple Gameplay:** Roll a six-sided die and accumulate points.
- **Risk and Reward:** Lose turn points on a 1 and reset score on consecutive 6s.
- **Score Tracking:** Keeps track of scores until a player reaches the target score.
- **Input Validation:** Enhanced version prompts with examples and repeatedly asks for valid input.
- **Round-Based Play:** Supports multiple rounds with summary displays.
- **Clear Instructions:** Both versions display easy-to-follow menu options and game rules.

## Requirements

- Python 3.6 or higher.

## How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/Pig_Dice_Game.git
   cd Pig_Dice_Game
   ```

2. **Run the Original Version:**
   ```bash
   python Pig_Dice_game.py
   ```

3. **Run the Enhanced Version:**
   ```bash
   python Pig_Dice_game_enhanced.py
   ```

## Gameplay Instructions

- **Rolling the Die:** Players take turns rolling a die. The outcome is displayed immediately.
- **Game Rules:**
  - **Rolling a 1:** The player loses all points accumulated during that turn.
  - **Two Consecutive 6s:** The player's total score resets to 0.
  - **Hold Option:** Players can choose to hold, adding the turn score to their total.
- **User Input Examples:**  
  In the enhanced version, prompts include examples (e.g., "Enter the number of players (e.g., 2)") to help ensure correct input.

## Differences Between the Versions

- **Original Version:**
  - Basic implementation with minimal input validation.
  - Fewer instructions for handling invalid inputs.

- **Enhanced Version:**
  - Robust input validation and error handling; the program continues to prompt until valid input is provided.
  - Prompts include clear examples to guide the user.
  - Improved code structure with type hints and detailed docstrings for maintainability.
  - Overall, a more user-friendly and resilient version of the game.

## Contributing

Contributions, bug reports, and feature requests are welcome! Please fork the repository and submit a pull request with your enhancements. For any issues, open an issue in the repository.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

Enjoy playing Pig Dice and have fun rolling the dice!
