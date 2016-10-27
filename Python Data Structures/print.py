text = raw_input("Enter a file name: ")
texted = open(text)
inside = texted.read()
inside = inside.upper()
inside = inside.rstrip()
print inside
