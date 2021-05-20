# the program prints character of the word from the end
count = -1
st = input("Enter the word: ")
length = len(st) * -1
while True:
    if count == length - 1:
        break
    char = st[count]
    print(char)
    count = count - 1
