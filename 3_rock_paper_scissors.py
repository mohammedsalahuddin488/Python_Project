import random
user_win = 0
computer_win = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type  Rock/Paper/Scissors or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)      # 0 = rock, 1 = paper, 2 = scissors
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick} .")

    if user_input == "rock" and computer_pick == "scissers":
        print("You Win")
        user_win += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You Win")
        user_win += 1

    elif user_input == "scissers" and computer_pick == "paper":
        print("You Win")
        user_win += 1

    else:
        print("You Lost! ")
        computer_win += 1

print(f"You won {user_win} times.")
print(f"Computer Won {computer_win} times.")
print("Good bye! ") 