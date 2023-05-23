num = [1,5,3,2,6,7]

def insertion_sort(arr) :
    for i in range(1,len(arr)) :
        for j in range(i,0,-1) :
            if (arr[j-1] > arr[j]) :
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else :
                break
        print(arr)
    return arr

print(insertion_sort(num))