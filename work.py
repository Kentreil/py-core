h = raw_input("How many hours did you work this week? ")
try:
    hours = float(h)
except Exception, e:
    print "You didn't enter a number"
    quit()
r = raw_input("What is your hourly rate? ")
try:
    rate = float(r)
except Exception, e:
    print "You didn't enter a number"
    quit()
if rate < 0 or hours < 0:
    print "Please enter numbers only"
else:
    if hours > 40:
        pay = (hours - 40) * rate * 1.5 + (40 * rate)
        print "You earned: $", pay
    else:
        pay = hours * rate
        print "You earned: $", pay
