import urllib
import xml.etree.ElementTree as ET
total = 0
grab = urllib.urlopen('http://python-data.dr-chuck.net/comments_275716.xml')
data = grab.read()
stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
for item in lst:
    one = item.find('count').text
    two = int(one)
    total = total + two
print total
