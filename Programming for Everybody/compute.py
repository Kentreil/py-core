def computepay(a, b):
    try:
        hours = float(a)
        rate = float(b)
    except:
        print "Please enter numbers only!"
        quit()
    if hours > 40:
        pay = (hours - 40) * rate * 1.5 + (40 * rate)
        print "You earned: $", pay
    else:
        pay = hours * rate
        print "You earned: $", pay
h = raw_input("How many hours did you work this week? ")
r = raw_input("What is your hourly rate? ")
computepay(h, r)
