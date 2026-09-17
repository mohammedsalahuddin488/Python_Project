try:
    print("Simple Calculator")

    a = int(input("Enter a 1st number:"))
    
    b = int(input("Enter a 2nd number:"))

    o = input("Chose an operation (+,-,*,/) :  ")

    match o:
        case "+":
            print(f"The result is {a + b}")
        case "-":
            print(f"The result is {a - b}")
        case "*":
            print(f"The result is {a * b}")
        case "/":
            print(f"The result is {a / b}")
        case "%":
            print(f"The result is {a % b}")
        case default:
            print("Invalid operation")

except Exception as e:
    print("Enter a valid number for a and b ")