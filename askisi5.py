def calc():
    global left
    global right
    global func
    l=int(left)
    r=int(right)
    if (func=='plus'):
        print(left,'+',right,'=',l + r)
    elif (func=='minus'):
        print(l - r)
    elif (func=='times'):
        print (l * r)
    else:
        print('Error: Not valited function!')

def check(q):
    if (q=="zero"):
        zero()
    elif (q=="one"):
        one()
    elif (q=="two"):
        two()
    elif (q=="three"):
        three()
    elif (q=="four"):
        four()
    elif (q=="five"):
        five()
    elif (q=="six"):
        six()
    elif (q=="seven"):
        seven()
    elif (q=="eight"):
        eight()
    elif (q=="nine"):
        nine()

def num(z):
    global left
    global right
    try:
        if (left!=''):
            right=z
            return right
        else:
            left=z
            return left
    finally:
        if ((left!='') and (right!='')):
            calc()

def zero():
    num('0')

def one():
    num('1')

def two():
    num('2')

def three():
    num('3')

def four():
    num('4')

def five():
    num('5')

def six():
    num('6')

def seven():
    num('7')

def eight():
    num('8')

def nine():
    num('9')


left=''
right=''
func=input("PLease give a function (plus, minus, times): ")
x=input("Please give a number from 0-9 (e.g: seven): ")
check(x)
y=input("Please give a number from 0-9 (e.g: three): ")
check(y)
