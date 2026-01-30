import random


player1_score = 0
player2_score = 0


def roll_die():
    return random.randint(1,6)

def turn(player_score):
    turn_total = 0
    print(f"Total Score: {player_score}")
    while True:
        move = input("Do you want to Roll or Hold (R or H): ").capitalize()

        if move == "R":
            roll = roll_die()
            print(f"You rolled a {roll}")

            if roll == 1:
                print("Turn over. No points.")
                return 0

            turn_total += roll
            print(f"Turn Total: {turn_total}")
            print(f"Total Score: {turn_total + player_score}")
            if turn_total + player_score > 100:
                return turn_total
            

        elif move == "H":
            return turn_total

        else:
            print("Invalid input. Try again.")

while player1_score < 100 and player2_score < 100:
    if player1_score < 100 and player2_score <= 100:
        print("Player One")
        player1_score += turn(player1_score)
    else:
        print("Player One Wins")
        break
    if player1_score < 100 and player2_score <= 100:
        print("Player Two")
        player2_score += turn(player2_score)
    else:
        print("Player 2 Wins")
        break


