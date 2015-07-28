while True:
    try:
        number = int(input("your fev number"))
        print(10000/number)
        break
    except ValueError:
        print("Please enter a number")
    