maximum = 0
minimum = 0
# the above are variable representing min and maximum values
while True:
    x = input("Enter a number: ")
    print(x.lower())
    if x == 'done':
        print("its done")
        break

    else:
        try:
            x = int(x)
            if maximum < x or maximum == 0:
                maximum = x
            if minimum > x or minimum == 0:
                minimum = x


        except ValueError:
            print("Invalid input, this is not a number !!!!")


print(f'Minimum number: {minimum}, Maximum number: {maximum}')