total = 0
count = 0
average = 0
# the while loop to help us interate through the commands
while True:
    x = input("Enter a number: ")
    if x == 'done':
        break

    else:
        try:
            x = float(x)
            count = 1 + count
            print("its done")
            total = total + x
            average = total/count
            continue
        except ValueError:
            print("Invalid input, this is not a number !!!!")


print(f'Your total: {total}, count: {count}, Average: {average}')