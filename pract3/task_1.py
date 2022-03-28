#1 whitespace before '('.
def plus (x, y):
    return (x + y)

#2 missing whitespace around operator.
def plus(x, y):
    a = x+y
    return (a)

#3 missing whitespace after ','.
def plus(x,y):
    return (x + y)

#4 unexpected spaces around keyword / parameter equals.
def plus(x = 5, y =10):
    return (x + y)

#5 expected 2 blank lines, found 1.
def some_message():
    print("Hello, world!")

def one_more_message():
    print("Hello, python!")

#6 multiple statements on one line (colon).
def equals(a, b):
    if (a == b): return "TRUE"

#7 multiple statements on one line (semicolon).
a = 10; b = 10; print(equals(a, b))

#8 comparison to None should be 'if cond is None:'.
number = False
if number != True:
    print("var is not equal to True")
if number == None:
    print("var is equal to None")

#9 comparison to True should be 'if cond is True:' or 'if cond:'.
number = True
if number == True:
    print('True!')
