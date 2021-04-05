# A program prompts the user to enter his/her name and tells the weather they can vote
try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You can vote")
    elif age > 0:
        print("Too young to vote")
    else:
        print("You are a time traveller")
except ValueError:
    print("no age in decimals")

