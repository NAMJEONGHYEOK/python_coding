import random

num = [1,4,5,2,8,6,9,7]

def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot_index = random.randint(0,len(arr)) # random(n,m) = n~ m-1까지 난수생성
        pivot = arr[pivot_index]
        # pivot = arr[len(arr) // 2] # 피벗을 중앙으로 잡음
        left, right, equal = [], [], []
        for i in arr:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                equal.append(i)

            print("l:{}, c:{}, r{}".format(left,equal,right))        
        return quick_sort(left) + equal + quick_sort(right)


print(quick_sort(num))

# 퀵 정렬에서 피봇을 랜덤으로 잡지 않는 경우 O(N2) 의 복잡도를 가진다
