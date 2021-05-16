i =99
while(True):
    if i>0:
        print("{0} bottles of beer on the wall, {0} bottles of beer.".format(i))
        i-=1
        print( "Take one down, pass it around, {0} bottles of beer on the wall...".format(i))
    elif i==0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        i=99
        print("Go to the store and buy some more, {0} bottles of beer on the wall...".format(i))
        break