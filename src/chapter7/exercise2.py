# the programm prints the average spam confidence
count = 0
total_spam_confidence = 0
average_spam_confidence = 0
file_name = input("Enter a file name: ")
try:
    file_handle = open(file_name)
    for line in file_handle:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            new_line = line.find(' ')
            num = line[(new_line + 1):]
            num = float(num)
            count = count + 1
            total_spam_confidence = total_spam_confidence + num
            average_spam_confidence = round((total_spam_confidence / count), 12)
    print("Average Spam Confidence: ", average_spam_confidence)
except:
    print("Invalid file name. File may not exist. Please consider including file extension")
    quit()
