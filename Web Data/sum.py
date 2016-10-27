import re
file = open("regex_sum_275714.txt")
text = file.read()
added = 0
stuff = re.findall('[0-9]+', text)
for i in stuff:
    added = added + int(i)
print added
