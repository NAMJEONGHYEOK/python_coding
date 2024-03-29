import sys

result=[]
def merge_sort(arr) :

    if len(arr) < 2 :
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merge_arr = []    
    l=r=0
    while l<len(left) and r<len(right) :
        if left[l] < right[r] :
            merge_arr.append(left[l])
            l += 1
        else :
            merge_arr.append(right[r]) 
            r += 1
    merge_arr += left[l:]
    merge_arr += right[r:]
    return merge_arr

num = int(sys.stdin.readline())
nlist = []
for _ in range(num) :
    nlist.append(int(sys.stdin.readline()))

result = merge_sort(nlist)

for i in result :
    print(i)