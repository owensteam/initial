# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0
float(sum)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    marker = line.find(":")
    stringValue = line[marker + 1:]
    floatValue = float(stringValue)
    sum = sum + floatValue
    
print "Average spam confidence:", (sum/count)