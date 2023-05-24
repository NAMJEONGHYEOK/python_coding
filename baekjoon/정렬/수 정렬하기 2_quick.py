def quick_sort(arr) :
    if len(arr) < 2 : 
        return arr
    
    pivot = arr[len(arr)//2]
    left = []
    right = []
    equal = []

    for i in arr :
        if i > pivot :
            right.append(i)
        elif i < pivot :
            left.append(i) 
        else :
            equal.append(i)
    return quick_sort(left)+equal+quick_sort(right)

n = int(input())
num = []
for _ in range(n) :
    num.append(int(input()))
    
result = quick_sort(num)

for i in result :
    print(i)

    