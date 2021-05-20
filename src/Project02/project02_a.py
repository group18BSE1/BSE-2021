#prompts the user for the output filename
#the loop will allow a user to re-enter a file with .txt in case of any errors

while True:
    output_file = input('Enter your file name:')
    if output_file[-4:] == '.txt':
        break
    else:
        print('The file name should have a .txt file extension')
inp = input('Enter the year:').lower()
#if the file cant be opened, returns error message and the progamme halts
try:
    #for '','all' and 'ALL'
    if inp=='' or input == 'all':
        with open('measles.txt','r') as main_file:
            with open(output_file,'w') as output:
                for line in main_file:
                    output.write(line)
    #for specifics
    elif inp.isdigit():
        with open('measles.txt','r') as main_file:
            with open(output_file,'w') as output:
                for line in main_file:
                    year = line[-5:]
                    if year.startswith(inp):
                        output.write(line)
except FileNotFoundError:
    print('Cant open file')
    exit()