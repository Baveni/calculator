print "Welcome to my calculator, it can only perform basic math such as +, -, *, /,, enjoy :)"
print "Please puch in the numbers you want to calculate-->>"
while True:

    x = raw_input("Please punch in the first number!")
    operator = raw_input("Please punch in youre operator!")
    y = raw_input("Please punch in the second number!")

    x = float(x)
    y = float(y)

    if operator == "+":
        print x + y
    elif operator == "-":
        print x - y
    elif operator == "*":
        print x * y
    elif operator == "/":
        print x / y
