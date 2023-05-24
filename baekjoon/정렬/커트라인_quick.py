def quick_sort(arr) :
    if len(arr) < 2 :
        return arr

    pivot = arr[len(arr)//2]
    left =[]
    right = []
    equal = []
    for i in arr :
        if i > pivot :
            left.append(i)
        elif i < pivot :
            right.append(i)
        else :
            equal.append(i)
    return quick_sort(left)+equal+quick_sort(right)

N, K = map(int,input().split())

num = list(map(int,input().split()))

# 내림차순 정렬 후 인덱스 k-1 출력
result = quick_sort(num)

print(result[K-1])

