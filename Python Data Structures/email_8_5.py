input = open("mbox-short.txt")
count = 0
for line in input:
    if line.startswith("From "):
        full = line.rstrip()
        part = full.split()
        count = count + 1
        print part[1]
print "There were", count, "lines in the file with From as the first word"
