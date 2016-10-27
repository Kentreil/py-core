import re
example = open("mbox-short.txt")
for line in example:
    line = line.rstrip()
    if re.search("^From:", line):
        print line
