print "Welcome to my calculator, it can only perform basic math such as +, -, *, /,, enjoy :)"
print "Please do your calculations."

answer = "Y"

while answer == "Y":

    x = raw_input("Please punch in the first number-->>")
    operator = raw_input("Please punch in youre operator-->>")
    y = raw_input("Please punch in the second number-->>")

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

    while True:
        print "if you want to perform more calculations, please type Y or N"
        answer = raw_input().upper()

        if answer not in "YN":
            print "you have to type Y or N"
        else:
            break
print "Thank you for using my calculator! Hope it served you well :)"