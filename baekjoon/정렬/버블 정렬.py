num = [1,4,5,2,3]

def bubble_sort(arr) :
    for i in range(len(arr)-1,0,-1) : 
        for j in range(i) :
            if(arr[j]>arr[j+1]) :
                arr[j],arr[j+1] = arr[j+1],arr[j] # swap
            print(arr)
    return arr

print(bubble_sort(num))