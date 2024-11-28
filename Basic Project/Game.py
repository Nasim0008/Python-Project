"""
This is just a normal Number Guessing Game.
Game Plan:
In this game, the computer generate a random number and I have to find the that number by using finite number of moves
Date: 28 November,2024
Developer Name : Md Nasim Hossen
"""
import random #import the random module
Random_Number = int(random.randrange(1,101)) # Generate a random number
Name = input("Please,Enter Your Name: ")
Number_of_Moves = 1
print("Please, Enter a random Number: ")
while True:
    value = int(input())
    if value == Random_Number:
        print(f"Congratulation {Name}, You won the Game!!")
        break
    if Number_of_Moves == 5:
        print(f"Game Over!!,{Name}")
        break
    elif value < Random_Number:
        print("Please Enter larger number: ")
    else:
        print("Please, Enter Smaller Number: ")
    Number_of_Moves = Number_of_Moves+1
