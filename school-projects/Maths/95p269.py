
def U_n(n):
    u = 0.7
    for i in range(1,n+1):
        u = (i+1)*u-1
        print("u(",i+1,") =",u)

U_n(12)