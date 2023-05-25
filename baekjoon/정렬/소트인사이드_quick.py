# # sol 1 : quick sort 연습
# import random
# num = list(input())
# for i in range(len(num)) :
#     num[i] = int(num[i])


# def quick_sort(arr) :
#     n = len(arr)
#     if n < 2:
#         return arr
#     pivot_index = random.randint(0,n-1)
#     pivot = arr[pivot_index]
#     left = []
#     right =[]
#     equal = []

#     for j in arr :
#         if j < pivot :
#             left.append(j)
#         elif j > pivot :
#             right.append(j)
#         else :
#             equal.append(j)

#     # return quick_sort(left)+equal+quick_sort(right) # 오름차순
#     return quick_sort(right)+equal+quick_sort(left) # 내림차순


# # print(quick_sort(num))
# num = quick_sort(num)
# for k in num :
#     print("%d" % k, end="")


# list 기본 정렬 사용, sol 2

num = list(input())
for i in range(len(num)) :
    num[i] = int(num[i])
num.sort(reverse=True)
for k in num :
    print("%d" % k, end="")