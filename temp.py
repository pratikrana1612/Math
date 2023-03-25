import math

def equation(x):
    # return (math.pow(x,3))-(5*x)+3
    # return (math.pow(x,3)+4*(math.pow(x,2))-10)
    # return (math.pow(x,3)-7*(math.pow(x,2))+14*x-6)
    return x*math.cos(x)-2*math.pow(x, 2)+3*x-1

def find_third(first,second,funfirst,funsecond):
    return ((first*funsecond)-(second*funfirst))/(funsecond-funfirst)

print(find_third(0.6060,1,0.0041,-1.4597))
# print(equation(1.3))