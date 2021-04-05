try:
    number = int(input("Enter number of people attending: "))
    if number <= 50:
        print("Pay $4,000")
    elif number <= 100:
        print("Pay $10,000")
    elif number <= 200:
        print("Pay $15,000")
    else:
        print("Pay $20,000")
except ValueError:
    print("Enter number in figures not words")

