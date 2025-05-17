import random

print("Welcome to number gusser game!")

expected_number = int(input("Enter the number between 1 to 10"))
round = 0

while True:
    if expected_number == random.randint(1,10):
        print("Correct guess!")
        round = round+1
        break
    expected_number = int(input("Try again"))    

