# quickSort
numbers = [40, 35, 27, 75, 50, 74, 77,60]
def quickSort(array):
    if len(array) < 2: 
        return array   
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot ]
        greater = [x for x in array[1:] if x > pivot ]
        return quickSort(less) + [pivot] + quickSort(greater)

result = quickSort(numbers)
print(result)