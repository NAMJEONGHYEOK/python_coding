# 
x,y,w,h = map(int,input().split())


min1 = 0
min2 = 0
if ((w-x) >=x) :
    min1 = x
else :
    min1 = w - x

if (h-y>=y) :
    min2 =y
else :
    min2 = h - y

if (min1 > min2) :
    print(min2)
else :
    print(min1)
