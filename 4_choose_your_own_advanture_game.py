name = input("Enter your Name: ")
print(f"Welcome {name} to this Adventure! ")

q1 = input("You are on a dirt road, it has come to an end and you can go left or right. Wich way you would like to go? ").lower()

if q1 == "left":
    q2 = input("You came to a river, you can walk around it or swin accross? type walk to walk around and swim to swin across.")

    if q2 == "swim":
        print("You swiming across the river and eaten by an alligator")
    elif q2 == "across":
        print("you walked for 2 km and rann out of water and lost the game")
    else:
        print("Not a valid option. You lose.")

    
elif q1 == "right":
    q3 = input("You came to a bridge it look like wabally do you want to cross or walk back.")
    if q3 == "cross":
        q4 = input("You crossed it and you saved your life from wild animals, and you met a stranger after the bridge do you tock to them yes or no")

        if q4 == "yes":
            print("Now you are totally safe hw will drop you at the police station.")
        elif q4 == "no":
            print("now you have to servive alone and you die")
        else:
            print("Not a valid option. You lose.")

    elif q3 == "back":
        print("You were killed by the wild animals")
    else:
        print("Not a valid option. You lose.")


else:
    print("Not a valid option. You lose.")
    
print("you loos the game.")
print(f"Thank you for playing {name}")