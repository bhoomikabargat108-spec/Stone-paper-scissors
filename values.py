
import random
def Values():
    u_turn = int(input("Your turn:"))
    if u_turn ==1:
        u_choice = 'stone'
    elif u_turn == 2:
        u_choice = 'paper'
    elif u_turn == 3:
        u_choice = 'scissors'
    ch = ["stone", "paper", "scissors"]
    c_turn = random.choice(ch)
    print("Computer's turn:", c_turn)
    
    return u_turn, c_turn,u_choice
