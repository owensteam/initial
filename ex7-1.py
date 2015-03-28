fileName = raw_input("Please enter the name of the file you wish to open:\n")

try:
    fh = open(fileName, 'r')
except:
    print("Error 1")
try:
    for line in fh:
        fileString = line.rstrip()
        fileStringUpper  = fileString.upper()
        print(fileStringUpper)
except:
    print("Error 2")

