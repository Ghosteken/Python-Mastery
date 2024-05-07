def play_round(player1_choice, player2_choice, scores):
    if player1_choice == player2_choice:
        print("It's a tie!")
    elif (player1_choice == "rock" and player2_choice == "scissors") or (player1_choice == "paper" and player2_choice == "rock") or (player1_choice == "scissors" and player2_choice == "paper"):
        print("Player 1 wins!")
        scores["Player 1"] += 1
    else:
        print("Player 2 wins!")
        scores["Player 2"] += 1

def get_masked_choice(player):
    choice = input(f"Enter your choice for {player} (rock, paper, scissors): ").lower()
    masked_choice = "*" * len(choice)
    print(f"{player}'s choice: {masked_choice}")
    return choice

def play_tournament(player1, player2, rounds):
    scores = {"Player 1": 0, "Player 2": 0}

    for i in range(rounds):
        print(f"\nRound {i + 1}:")
        play_round(player1, player2, scores)

    return scores

def main():
    print("Welcome to the Rock, Paper, Scissors Tournament!")

    player1_choices = []
    player2_choices = []

    for i in range(3):  # Semi-finals
        print(f"\nSemi-finals - Round {i + 1}:")
        player1_choices.append(get_masked_choice("Player 1"))
        player2_choices.append(get_masked_choice("Player 2"))

    semi_finals_scores = play_tournament(player1_choices[-1], player2_choices[-1], 3)

    if semi_finals_scores["Player 1"] > semi_finals_scores["Player 2"]:
        print("Player 1 advances to the finals!")
        finals_winner = "Player 1"
    elif semi_finals_scores["Player 2"] > semi_finals_scores["Player 1"]:
        print("Player 2 advances to the finals!")
        finals_winner = "Player 2"
    else:
        print("Semi-finals resulted in a tie. Restart the tournament.")
        return

    print("\nFinals:")
    player3_choices = []
    player4_choices = []

    for i in range(5):  # Finals
        print(f"\nFinals - Round {i + 1}:")
        player3_choices.append(get_masked_choice("Player 3"))
        player4_choices.append(get_masked_choice("Player 4"))

    finals_scores = play_tournament(finals_winner, play_round(player3_choices[-1], player4_choices[-1], {}), 5)

    print("\nOverall Winner:")
    if finals_scores[finals_winner] > finals_scores["Player 2"]:
        print(f"{finals_winner} is the Overall Winner!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
     main()
