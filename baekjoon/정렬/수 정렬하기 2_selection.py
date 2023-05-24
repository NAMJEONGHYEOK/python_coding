def selection_sort(arr) :
    n = len(arr)
    for i in range(n-1) :
        c_index = i
        for j in range(i+1,n) :
            if (arr[c_index] < arr[j]) :
                c_index = j # 인덱스바꾸고
        arr[c_index],arr[i] = arr[i],arr[c_index]
    return arr

n = int(input())
num = []
for i in range(n) :
    num.append(int(input()))

result = selection_sort(num)

for i in result :
    print(i)


    ## 범위가 백만이므로 시간초과의 여지가 있다. 최악일경우 O(n2)일 경우는 1억임.
