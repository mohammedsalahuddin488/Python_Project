print("Welcome to the quizz !")

playing = input("Do you want to play the quizz? ")

if playing.upper() != "YES":
    print("Play Next Time")
    quit()     

print("OK Continue to play Quizz! ")
score = 0

answer = input("Which library is commonly used for data analysis in Python? ")
if answer.lower() == "pandas":
    print("Correct ! ")
    score += 1
else:
    print("Incorrect ! ")
    print("* Correct Answer = pandas")


answer = input("Which keyword is used to define a function in Python? ")
if answer.lower() == "def":
    print("Correct ! ")
    score += 1
else:
    print("Incorrect ! ")
    print("* Correct Answer = def")
    

answer = input("Which component is commonly used to control a robot's movement? ")
if answer.lower() == "motor":
    print("Correct ! ")
    score += 1
else:
    print("Incorrect ! ")
    print("* Correct Answer = motor")


answer = input("Which language is widely used in AI development? ")
if answer.lower() == "python":
    print("Correct ! ")
    score += 1
else:
    print("Incorrect ! ")
    print("* Correct Answer = python")

print(f"Your Total Score out of 4 = {score}")
print(f"Your Total % is = {(score/4 )*100}")