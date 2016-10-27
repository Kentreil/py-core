smallest = None
largest = None
while True:
    num = raw_input("Enter a number")
    if num == "done":
        break
    try:
        num = int(num)
    except Exception, e:
        print "Invalid input"
        continue
    if smallest is None:
        smallest = num
        largest = num
    elif smallest > num:
        smallest = num
    elif num > largest:
        largest = num
print "Maximum is ", largest
print "Minimum is ", smallest
