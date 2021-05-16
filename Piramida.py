import math

n=int(input("Wprowadź liczbę: "))

a="*"
b=" "

if n%2==0:
    c = 2
    for i in range(math.ceil(n/2)):
        print((n - 2) * b, c * a)
        n -= 1
        c += 2

else:
    c = 1
    for i in range(math.ceil(n/2)):
        print ((n-2)*b, c*a)
        n-=1
        c+=2
