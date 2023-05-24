def bubble_sort(arr) :
    n = len(arr)
    for i in range(n - 1): # 비교제어
        for j in range(n - 1 - i): # 인덱스 순회
            if (arr[j] > arr[j+1]) :
                arr[j],arr[j+1] = arr[j+1],arr[j]
                # print(arr)
        # print(i)
    return arr



n = int(input())


num = []
# input은 1000 이하의 정수
for _ in range(n) :
    num.append(int(input()))

result = bubble_sort(num)

for i in result :
    print(i)