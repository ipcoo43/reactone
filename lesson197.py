# Bubble Sort
numbers = [7, 3, 2, 9, 4]

def bubbleSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr

print(bubbleSort(numbers))