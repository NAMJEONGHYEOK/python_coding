
repeat = 9
arr = []
for i in range(repeat) :
    a = int(input())
    arr.append(a)

maxValue = max(arr); 


for i,j in enumerate(arr) :
    if ( j == maxValue ) :
        print(j)
        print(i+1)

