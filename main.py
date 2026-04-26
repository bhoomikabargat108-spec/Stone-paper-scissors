from utils import menu
from values import Values

while True:
    menu()
    
    u_turn, c_turn,u_choice = Values()
    if u_choice == c_turn:
        print("Match is tie!\n ")
    elif (c_turn== 'paper' and u_choice == 'stone') or (c_turn == 'scissors' and u_choice == 'paper') or (c_turn == 'stone' and u_choice == 'scissors'):
        print("Computer is the winner!!\n")
    else:
        print("Hurray!! You are the winner ✧⁠◝⁠(⁠⁰⁠▿⁠⁰⁠)⁠◜⁠✧  \n")
