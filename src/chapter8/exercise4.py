# sorts and print a list alphabetical order
list = []
file = open("romeo.txt")
for line in file:
    wd = line.split()
    for word in wd:
        if word in list:
            continue
        list.append(word)
print(sorted(list))
