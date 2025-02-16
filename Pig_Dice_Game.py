import random

def roll_die():
    # """
    # Roll a six-sided die and return the result.
    # """
    return random.randint(1, 6)

def take_turn(player, current_score):
    # """
    # Take a turn for the player. Roll the die and accumulate points.
    # If a 1 is rolled, the player loses all points for that turn.
    # If two 6s are rolled consecutively, the player's score resets to 0.
    # The player can choose to 'hold' to secure their points.
    # """
    turn_score = 0
    previous_roll = 0
    while True:
        roll = roll_die()
        print(f"{player} rolled a {roll}")
        if roll == 1:
            print(f"{player} loses all points accumulated this turn.")
            return current_score
        elif roll == 6 and previous_roll == 6:
            print(f"{player} rolled two consecutive 6s. Score resets to 0.")
            return 0
        else:
            turn_score += roll
            print(f"{player}'s turn score: {turn_score}")
            choice = input("Enter 'r' to roll again or 'h' to hold: ").strip().lower()
            if choice == 'h':
                return current_score + turn_score
            previous_roll = roll

def pig_dice_game():
#     """
#     Main function to play the Pig Dice Game.
#     """
    num_players = int(input("Enter the number of players: ").strip())
    players = [input(f"Enter name for Player {i+1}: ").strip() for i in range(num_players)]
    scores = {player: 0 for player in players}
    goal_score = int(input("Enter the target score to win: ").strip())
    total_scores = {player: 0 for player in players}
    rounds_played = 0

    current_player = random.choice(players)
    while all(score < goal_score for score in scores.values()):
        print(f"\n{current_player}'s turn. Current score: {scores[current_player]}")
        scores[current_player] = take_turn(current_player, scores[current_player])
        if scores[current_player] >= goal_score:
            print(f"{current_player} wins this round with a score of {scores[current_player]}!")
            total_scores[current_player] += 1
            rounds_played += 1
            print("\nRound Summary:")
            for player, score in scores.items():
                print(f"{player}: {score} points")
            print("\nTotal Scores:")
            for player, score in total_scores.items():
                print(f"{player}: {score} round wins")
            if input("Do you want to play another round? (y/n): ").strip().lower() != 'y':
                break
            scores = {player: 0 for player in players}
        else:
            current_player = players[(players.index(current_player) + 1) % num_players]

    print("\nFinal Scores:")
    for player, score in total_scores.items():
        print(f"{player}: {score} round wins")
    print("Game over!")

if __name__ == "__main__":
    pig_dice_game()