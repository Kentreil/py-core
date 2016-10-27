text = "X-DSPAM-Confidence:    0.8475"
front = text.find("0")
back = text.find("5") + 1
output = text[front:back + 1]
output = float(output)
print output
