input = open("romeo.txt")
words = list()
for line in input:
    single = line.split()
    for i in single:
        if i not in words:
            words.append(i)
words.sort()
print words
