# prompt the user to enter the file name and process it in uppercase while removing spaces at the end
fname = input("Enter a file name: ")
try:
    handle = open(fname)
    for line in handle:
        line = line.rstrip()
        line= line.upper()
        print(line)
except:
    print("Invalid file name. File may not exist. Please consider including file extension")
    quit()
