a, b, c = map(int,input().split())

value = 0


if (a == b == c) :
    value = a * 1000 + 10000
elif (a == b ) :
    value = a * 100 + 1000
elif (a == c ) :
    value = a * 100 + 1000
elif (b == c ) :
    value = b * 100 + 1000
else :
    value = 100 * max(a,b,c)

print(value)
