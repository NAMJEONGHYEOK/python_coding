def quick_sort(arr) :
    if len(arr) < 2 :
        return arr
    
    pivot = arr[len(arr) // 2]
    left = []
    right = []
    equal = []

    for i in arr :
        if i < pivot :
            left.append(i)
        elif i > pivot :
            right.append(i)
        else :
            equal.append(i)
    
    return quick_sort(left) + equal + quick_sort(right)



num = []
for i in range(5) :
    num.append(int(input()))

result = quick_sort(num)

sum = sum(result)
avg = sum // 5
middle = result[2] # 5개의 정수중 중앙값은 3번째 수이다.

print(avg)
print(middle)