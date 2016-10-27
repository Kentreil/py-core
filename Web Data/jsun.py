import urllib
import json
total = 0
start = raw_input("Enter Web Adress: ")
site = urllib.urlopen(start).read()
first = json.loads(site)
for item in first:
    number = item["count"]
    number1 = int(number)
    total = total + number1
print total
