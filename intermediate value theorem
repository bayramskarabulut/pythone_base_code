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
    
    print(i, " tahmin ", (b-a)/2, " hatı payı" )
    
    if (b-a)/2 < e:
        print("hata payı ", (b-a)/2, "tahmin ", (b+a)/2)
        break
    
    if (abs(ax)/ax) + (abs(ix)/ix):
        a = i
        ax = funcx(a)
    elif (abs(bx)/bx) + (abs(ix)/ix):
        b = i
        bx = funcx(b)
    else:
        print("doğru sayı", i)
        break 
    
    
