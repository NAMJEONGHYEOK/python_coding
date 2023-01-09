a, b = map(int, input().split())
arr = []

c = list(map(int,input().split()))
arr.extend(c)

for j in arr :
    if (j < b) :
        print("%d" % j ,end=" ")
    else :
        continue

