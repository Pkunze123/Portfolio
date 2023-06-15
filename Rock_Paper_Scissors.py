from getpass import getpass

print("Epic Rock-Paper-scissors Battle")
print("Input answer at your own peril!")
print("+++++++++++++++++++++++++++++++")

score_player_1 = 0
score_player_2 = 0

while score_player_1 < 3 and score_player_2 < 3:
    player_1 = getpass(
        "Player 1, What do you pick? R - Rock, P = paper, S = scissors\n").lower()
    player_2 = getpass(
        "Player 2, What do you pick? R - Rock, P = paper, S = scissors\n").lower()

    if player_1 == player_2:
        print("It's a tie!")
    elif player_1 == "r" and player_2 == "s" or player_1 == "p" and player_2 == "r" or player_1 == "s" and player_2 == "p":
        score_player_1 += 1
        print("Player 1 wins!")
    elif player_1 in ['r', 'p', 's'] and player_2 in ['r', 'p', 's']:
        score_player_2 += 1
        print("Player 2 wins!")
    else:
        print("Something went wrong... Please make sure to only type the correct first letter of your choice.")

    print(f"Score: Player 1 = {score_player_1}, Player 2 = {score_player_2}")

if score_player_1 == 3:
    print("Player 1 wins the game!")
else:
    print("Player 2 wins the game!")
