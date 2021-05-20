word = input("Enter the word: ")
character = input("enter character\n")


def counts():
    count = 0
    for wd in word:
        if wd == character:
            count = count + 1
    return count


print(counts())

