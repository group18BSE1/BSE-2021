# input section
location = input("Enter location: ")
try:
    pay = int(input("Enter pay: "))
    if location == "Kampala":
        if pay >= 10000000:
            print("sure i can work with this")
        else:
            print("No way")
    if location == "Mbarara":
        if pay > 4000000:
            print("sure i can work with this")
        else:
            print("No thanks, i can find some thing better")
    if location == "space":
        print("sure i can work with this")
    else:
        if pay >= 6000000:
            print("sure i can work with this ")
        else:
            print("no thanks, i can find something else")

except ValueError:
    print("Enter pay in digits")


