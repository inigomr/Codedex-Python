import random

print("===================")
print("Rock Paper Scissors")
print("===================\n")

print("1) ✊")
print("2) ✋")
print("3) ✌️")
player = int(input("Pick a number: "))
computer = random.randint(1, 3)

if player == 1:
    print("You chose: ✊")
elif player == 2:
    print("You chose: ✋")
elif player == 3:
    print("You chose: ✌️")
else:
    print("Invalid input")

if computer == 1:
    print("CPU chose: ✊")
elif computer == 2:
    print("CPU chose: ✋")
elif computer == 3:
    print("CPU chose: ✌️")
else:
    print("Invalid input")

if player == computer:
    print("It's a tie!")
elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("You lost!")
elif (player == 2 and computer == 1) or (player == 3 and computer == 2) or (player == 1 and computer == 3):
    print("You win!")
else:
    print("Invalid input")