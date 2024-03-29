def merge_sort(arr) : # 병합 정렬 사용
    if (len(arr) < 2) :
        return arr
    
    mid = len(arr) //2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merge_arr = []
    l=r=0
    while l < len(left) and r < len(right) :
        if left[l] <right[r] :
            merge_arr.append(left[l]) 
            l += 1
        else : 
            merge_arr.append(right[r]) 
            r += 1
        
    merge_arr += left[l:]
    merge_arr += right[r:]
    return merge_arr

n = int(input())


num = []
# input은 1000 이하의 정수
for _ in range(n) :
    num.append(int(input()))

result = merge_sort(num)

for i in result :
    print(i)