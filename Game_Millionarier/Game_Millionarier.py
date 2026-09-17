questions = [
    ["Capital of India?", "Mumbai", "Hyderabad", "New Delhi", "Chennai", 3],
    ["Largest planet in our Solar System?", "Earth", "Jupiter", "Mars", "Venus", 2],
    ["How many days are there in a week?", "5", "6", "7", "8", 3],
        # ["Who is known as the Father of Computers?", "Charles Babbage", "Bill Gates", "Alan Turing", "Steve Jobs", 1],
        # ["Which language is used for web styling?", "Python", "HTML", "CSS", "Java", 3],
        # ["What is 10 + 20?", "20", "30", "40", "50", 2],
        # ["Which is the largest ocean?", "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", 3],
        # ["Which animal is known as the King of the Jungle?", "Tiger", "Lion", "Elephant", "Bear", 2],
        # ["How many continents are there?", "5", "6", "7", "8", 3],
        # ["What is the chemical symbol for water?", "CO2", "O2", "H2O", "NaCl", 3]
]

score = 0

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    a = int(input("Choose the correct answer. 1 is for a, 2 is for b, 3 is for c, 4 is for d :"))
    if(question[5] == a):
        print("Correct!")
        total_score = score
        score += 1
    else:
        print("Incorrect!")
        print("Better luck next time!")
        break

print(f"your score is score: {score} out of {len(questions)}")
if total_score is 0:
    print("You have won 10,000")
elif total_score is 1:
    print("You have won 20,000")
else:
    print("You have won 30,000")