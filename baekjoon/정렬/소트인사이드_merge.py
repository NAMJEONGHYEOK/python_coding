import random
num = list(input())



for i in range(len(num)) :
    num[i] = int(num[i])


def merge_sort(arr) :
    n = len(arr) 

    if n < 2 :
        return arr 
    
    mid = n // 2
    left = merge_sort(arr[mid:])
    right = merge_sort(arr[:mid])

    merge_arr = []
    l=r=0

    while l<len(left) and r <len(right) :
        if left[l] > right[r] :  # merge 하여 넣을떄 크기 구분 오름차순,내림차순
            merge_arr.append(left[l])
            l += 1 
        else :
            merge_arr.append(right[r])
            r += 1



            
    merge_arr += left[l:]
    merge_arr += right[r:]
    return merge_arr

num = (merge_sort(num))
for k in num :
    print("%d" % k, end="")