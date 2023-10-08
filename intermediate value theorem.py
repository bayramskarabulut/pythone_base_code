a = 1
b = 2

def funcx(x):
    return x**2 - 2
    
e = 10**-4

ax = funcx(a)
bx = funcx(b)

while True:
    i = (a+b)/2
    ix = funcx(i)
    
    print(i, " 	ballpark figure ", (b-a)/2, " error margin " )
    
    if (b-a)/2 < e:
        print("error margin ", (b-a)/2, " ballpark figure ", (b+a)/2)
        break
    
    if (abs(ax)/ax) + (abs(ix)/ix):
        a = i
        ax = funcx(a)
    elif (abs(bx)/bx) + (abs(ix)/ix):
        b = i
        bx = funcx(b)
    else:
        print("single position ", i)
        break 
    
    
