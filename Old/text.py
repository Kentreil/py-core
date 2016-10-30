hours = float(raw_input('How many hours did you work this week? '))
rate = float(raw_input('What is your hourly rate? '))
if hours > 40:
    pay = (hours - 40) * rate * 1.5 + (40 * rate)
    print "Your pay will be:", pay, "Dollars"
else:
    pay = hours * rate
    print "Your pay will be:", pay, "Dollars"
