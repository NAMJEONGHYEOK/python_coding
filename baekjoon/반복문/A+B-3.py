TC = int(input())
sumlist = []
for i in range(TC) :
    a, b = map(int, input().split())
    sumlist.append(a+b)

for i in sumlist :
   print(i)