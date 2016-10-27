gd = raw_input("Please enter your grade ")
try:
    grade = float(gd)
except Exception, e:
    print "Please enter grade in a range of 1.0 - 0.0, Thanks!!"
    quit()
if grade > 1:
    print "Please enter grade in a range of 1.0 - 0.0, Thanks!"
    quit()
elif grade >= 0.9:
    print "Your grade is a A"
elif grade >= 0.8:
    print "Your grade is a B"
elif grade >= 0.7:
    print "Your grade is a C"
elif grade >= 0.6:
    print "Your grade is a D"
elif grade < 0.6:
    print "Your grade is a F"
