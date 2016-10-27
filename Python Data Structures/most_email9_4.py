texts = open("mbox-short.txt")
data = list()
for line in texts:
    if line.startswith("From "):
        words = line.rstrip()
        wordup = words.split()
        data.append(wordup[1])
counts = dict()
for i in data:
    counts[i] = counts.get(i, 0) + 1
Bigcount = None
Bigword = None
for i, count in counts.items():
    if Bigcount is None or count > Bigcount:
        Bigword = i
        Bigcount = count
print Bigword, Bigcount
