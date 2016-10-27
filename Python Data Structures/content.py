fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    text = line[21:26 + 1]
    added = float(text)
    total = total + added
    count = count + 1
adv = total / count
print "Average spam confidence:", adv
