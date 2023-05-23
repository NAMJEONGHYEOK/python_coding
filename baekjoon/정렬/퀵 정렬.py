num = [1,4,5,2,8,6,9,7]

def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2] # 피벗을 중앙으로 잡음
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