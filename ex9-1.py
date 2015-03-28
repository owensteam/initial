name = raw_input("Please enter filename: ")
fh = open(name)
counter = 0
diction = dict()
maxOcc = 0
for line in fh:
    words = line.split()
    if line.startswith('From '):
        diction[words[1]] = diction.get(words[1],0) + 1
for mailAdd,occ in diction.items():
    if occ > maxOcc:
        maxOcc = occ
        maxMailAdd = mailAdd
print maxMailAdd, maxOcc

    