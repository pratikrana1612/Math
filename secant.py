import math


def equation(x):
    # return (math.pow(x,3))-(5*x)+3
    # return (math.pow(x,3)+4*(math.pow(x,2))-10)
    # return (math.pow(x,3)-7*(math.pow(x,2))+14*x-6)
    # return math.pow(x,3)-25
    # return x-math.pow(2,-x)
    # return 2*x*(math.cos(2*x))-math.pow((x+1),2)
    # return round(x*math.cos(x)-2*math.pow(x, 2)+3*x-1,4);
    return math.cos(x)-3*(x)+1


prevans = 0
def find_third(first,second,funfirst,funsecond):
    return ((first*funsecond)-(second*funfirst))/(funsecond-funfirst)

def fun(first, second):
    global prevans
    i = 1
    third = 1
    while prevans != third:
        print(f"****{i} i****")
        print(f"{first}  {second}")
        prevans = third
        third = round(find_third(first,second,equation(first),equation(second)),4)
        first=third
        i += 1
    print(f"Answer:{third}")
    print(f"Iteration:{i}")


first = float(
    input("Enter first root which gets positive value when you enter in function:"))
second = float(
    input("Enter Second root which gets negative value when you enter in function:"))
fun(first, second)
