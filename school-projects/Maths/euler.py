def euler1(a,h):
    x=1
    y=0
    while x<a:
        x = x + h
        y = y + h / x
    print("f(",a,") = ",y,"avec h =",h)
    return

"""
euler1(2,1)
euler1(3,1)
euler1(7,1)
euler1(2,10)
euler1(3,10)
euler1(7,10)
"""

def euler2(a,h):
    x=1
    y=0
    if a>1:
        while x<a:
            x=x+h
            y+=h/x
    else:
        while x>a:
            x-=h
            y-=h/x
    print("f(",a,") = ",y,"avec h =",h) 
euler2(2,0.000001)