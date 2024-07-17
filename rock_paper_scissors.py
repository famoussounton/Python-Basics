#Implement a rock, paper, scissors game against the computer.
import random
import sys

def determine(a, b):
    if (a == b):
        return "It's a draw"
    elif (a == "rock" and b == "scissors") or (a== "scissors" and b == "paper") or (a == "paper" and b == "rock"):
        return "Player win"
    else:
        return "Computer win"

def func():
    list = ["rock", "paper", "scissors"]
    b_p = 0
    a_p = 0
    r = 3

    print("***** New game of Rock, Paper, Scissors *****")
    print(f" You will play {r} rounds. Enter your choice:")

    for num in range(r):
        print(f"Round {num + 1}")
        user_choice = input().lower()

        if (user_choice not in list):
            print("Invalid input, try again")
            continue

        b = random.choice(list)

        print(f"\nYour choice is: {user_choice}")
        print(f"Computer's choice is: {b}")

        result = determine(user_choice, b)
        print (result)
        if (result == "Player win"):
            a_p += 1
        elif (result == "Computer win"):
            b_p += 1

    print("******Game Over******")

    if(a_p > b_p):
        print("-----Congratulations, you win this game-----")
    elif(a_p < b_p):
        print("-----Computer won this game-----")
    else:
        print("-----It's a drawww-----")


if __name__ == "__main__":
    func()