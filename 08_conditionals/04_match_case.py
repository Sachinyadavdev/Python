a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You won a charger")
    case 3:
        print("You won $3")
    case 6:
        print("You won a camera")
    case _:
        print("Better luck next time")

age = 25

match age:
    case 25:
        print("Age is 25")

    case 18:
        print("Age is 18")

    case 10:
        print("Age is 10")

    case _:
       print("Printing the Default Case")
    
