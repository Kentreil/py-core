pull = open("mbox-short.txt")
abc = list()
for line in pull:
    if line.startswith("From "):
        words = line.split()
        word = words[5]
        abc.append(word)
time = list()
for i in abc:
    b = i[0:2]
    time.append(b)
count = dict()
for t in time:
    count[t] = count.get(t, 0) + 1
key = list()
for k, v in count.items():
    key.append((k, v))
key.sort()
for o, t in key:
    print o, t
