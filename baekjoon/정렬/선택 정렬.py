num = [1,5,3,2,4,7]

def selection_sort(arr) :
    for i in range(len(num)-1) :
        min_idx = i
        for j in range(i+1,len(num)) :
            if (arr[j] < arr[min_idx]) :
                min_idx = j 
        arr[i],arr[min_idx] = arr[min_idx],arr[i] # swap
        print(arr)
    return arr
print(selection_sort(num))