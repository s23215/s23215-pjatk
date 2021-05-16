import random

a= random.randint(0,100)
n=0
print (a)

while n!=a:
    n= int(input("Wprowadź liczbę:"))
    if n==a:
        print("W sam raz!")
    elif n>a:
        print ("Za dużo!")
    else:
        print ("Za mało!")

