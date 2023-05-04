a, b, c = map(int,input().split())
profit =  a // (c-b) + 1
if (profit > 0 ) :
    print(profit)
else :
    print("-1")
    