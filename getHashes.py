fileName = raw_input("Filename: ")
fh = open(fileName)
counter = 0
int(counter)
hashes = list()
words = list()
for line in fh:
    fullLine = line.split()
    #print words
    print fullLine[1]
    #for word in words:
    #    hashes[counter] = words[1]
    counter = counter + 1
#print hashes
#print words