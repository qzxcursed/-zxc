def bubble_sort(array_to_sort):
    n = len(array_to_sort)
    for i in range(n):
        for j in range(0, n-i-1):
            if array_to_sort[j] > array_to_sort[j+1]:
                array_to_sort[j], array_to_sort[j+1] = array_to_sort[j+1], array_to_sort[j]
    return array_to_sort

 array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(array)
print(sorted_array)

