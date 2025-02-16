import random
from typing import List

def get_valid_int(prompt: str, example: str = "") -> int:
    # """
    # Prompt the user for an integer input until a valid integer is entered.
    
    # Args:
    #     prompt (str): The prompt message to display.
    #     example (str): An example of valid input to show the user.
    
    # Returns:
    #     int: The valid integer entered by the user.
    # """
    while True:
        user_input = input(f"{prompt} (e.g., {example}): ").strip()
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_choice(prompt: str, choices: List[str], example: str = "") -> str:
    # """
    # Prompt the user to enter a valid choice from a list of allowed choices.
    
    # Args:
    #     prompt (str): The prompt message to display.
    #     choices (List[str]): A list of valid choices.
    #     example (str): An example of valid input.
    
    # Returns:
    #     str: The valid choice entered by the user.
    # """
    choices_lower = [choice.lower() for choice in choices]
    while True:
        user_input = input(f"{prompt} (e.g., {example}): ").strip().lower()
        if user_input in choices_lower:
            return user_input
        print(f"Invalid choice. Please enter one of {choices}.")

def roll_die() -> int:
    # """
    # Roll a six-sided die and return the result.
    
    # Returns:
    #     int: A random integer between 1 and 6.
    # """
    return random.randint(1, 6)

def take_turn(player: str, current_score: int) -> int:
    # """
    # Execute a turn for the given player. The player rolls a die repeatedly to 
    # accumulate points, but risks losing the turn's points if a 1 is rolled.
    # Two consecutive 6s will reset the player's score to 0.
    
    # Args:
    #     player (str): The name of the player.
    #     current_score (int): The player's current total score.
    
    # Returns:
    #     int: The updated total score after the turn.
    # """
    turn_score = 0
    previous_roll = 0
    print(f"\n{player}, it's your turn. Your current total score is {current_score}.")
    while True:
        roll = roll_die()
        print(f"{player} rolled a {roll}.")
        if roll == 1:
            print(f"Oh no! {player} rolled a 1 and loses all points accumulated this turn.")
            return current_score  # No points added this turn
        elif roll == 6 and previous_roll == 6:
            print(f"Unlucky! {player} rolled two consecutive 6s. Your total score resets to 0.")
            return 0
        else:
            turn_score += roll
            print(f"{player}'s turn score so far: {turn_score}.")
            choice = get_valid_choice(
                "Enter 'r' to roll again or 'h' to hold",
                choices=['r', 'h'],
                example='r'
            )
            if choice == 'h':
                updated_score = current_score + turn_score
                print(f"{player} holds. Your new total score is {updated_score}.")
                return updated_score
        previous_roll = roll

def pig_dice_game() -> None:
    # """
    # Main function to play the Pig Dice Game. Players take turns to roll the die and 
    # accumulate points until one of them reaches the target score.
    # """
    print("Welcome to the Pig Dice Game!")
    
    num_players = get_valid_int("Enter the number of players", example="2")
    players = []
    for i in range(num_players):
        while True:
            name = input(f"Enter name for Player {i+1} (e.g., Alice): ").strip()
            if name:
                players.append(name)
                break
            else:
                print("Player name cannot be empty. Please try again.")
    
    # Initialize scores for each player
    scores = {player: 0 for player in players}
    total_round_wins = {player: 0 for player in players}
    goal_score = get_valid_int("Enter the target score to win", example="100")
    
    # Randomly choose starting player
    current_player = random.choice(players)
    round_number = 1

    while all(score < goal_score for score in scores.values()):
        print(f"\n--- Round {round_number}: {current_player}'s turn ---")
        print(f"Current score for {current_player}: {scores[current_player]}")
        scores[current_player] = take_turn(current_player, scores[current_player])
        if scores[current_player] >= goal_score:
            print(f"\nCongratulations, {current_player}! You win this round with a score of {scores[current_player]}!")
            total_round_wins[current_player] += 1
            # Display round summary
            print("\nRound Summary:")
            for player, score in scores.items():
                print(f"{player}: {score} points")
            print("\nTotal Round Wins:")
            for player, wins in total_round_wins.items():
                print(f"{player}: {wins} wins")
            # Ask to play another round
            play_again = get_valid_choice("Do you want to play another round? (y/n)", choices=['y', 'n'], example='y')
            if play_again != 'y':
                break
            # Reset scores for new round
            scores = {player: 0 for player in players}
            round_number += 1
            # Optionally, choose a new starting player randomly
            current_player = random.choice(players)
            continue
        else:
            # Move to the next player's turn in round-robin fashion
            current_index = players.index(current_player)
            current_player = players[(current_index + 1) % num_players]

    print("\nFinal Round Wins:")
    for player, wins in total_round_wins.items():
        print(f"{player}: {wins} wins")
    print("Game over! Thanks for playing Pig Dice Game.")

if __name__ == "__main__":
    pig_dice_game()