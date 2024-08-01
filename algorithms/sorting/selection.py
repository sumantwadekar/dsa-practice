"""
Selection sort implementation
1. Here in every iteration, we find correct element for the first, second and so on indices
2. We first find the minimum element and then put it at 0th index
3. Then continue finding minimum element from remaining array and putting at correct index
"""


def selection_sort(arr):
    size = len(arr)
    for index in range(size):
        temp = index
        for inner in range(index + 1, size):
            if arr[temp] > arr[inner]:
                temp = inner
        if temp != index:
            arr[temp], arr[index] = arr[index], arr[temp]

    return arr


"""
Bubble sort impl
1. For every iteration, we compare adjacent elements and put the highest element at its correct position
"""
def bubble_sort(arr):
    size = len(arr)
    swap = False
    for index in range(0, size):
        for inner in range(size - index - 1, 0, -1):
            if arr[inner - 1] > arr[inner]:
                arr[inner - 1], arr[inner] = arr[inner], arr[inner - 1]
                swap = True
        if not swap:
            return arr
    return arr


"""
This is like cards game.
We divide array into two parts, one of them in sorted and another is unsorted
Take element from first index and put it at the right place in sorted array
"""
def insertion_sort(arr):
    size = len(arr)
    for index in range(1, size):
        temp = arr[index]
        inner = index - 1
        while((inner >= 0) and (arr[inner] > temp)):
            arr[inner + 1] = arr[inner]
            inner -= 1
        arr[inner + 1] = temp
    return arr

def merge(arr, start, mid, end):
    left = start
    right = mid+1
    temp_arr = []
    while (left <= mid) and (right <= end):
        if arr[left] > arr[right]:
            temp_arr.append(arr[right])
            right += 1
        else:
            temp_arr.append(arr[left])
            left += 1
    while(left <= mid):
        temp_arr.append(arr[left])
        left += 1
    while(right <= end):
        temp_arr.append(arr[right])
        right += 1
    # Copy elements back to original array
    for index in range(start, end+1):
        arr[index] = temp_arr[index-start]
    return arr


def merge_sort(arr, start, end):
    if start >= end:
        return arr
    mid = (start + (end)) // 2

    arr = merge_sort(arr, start, mid)
    arr = merge_sort(arr, mid + 1, end)
    arr = merge(arr, start, mid, end)
    return arr


def partition_index(arr, start, end):
    pindex = start
    pivot = arr[end]
    for index in range(start, end):
        if arr[index] <= pivot:
            arr[index], arr[pindex] = arr[pindex], arr[index]
            pindex += 1

    arr[pindex], arr[end] = arr[end], arr[pindex]
    return pindex


def quick_sort(arr, start, end):
    if start >= end:
        return arr
    index = partition_index(arr, start, end)
    quick_sort(arr, start, index-1)
    quick_sort(arr, index+1, end)
    return arr

print(quick_sort([11, 1, 25, 4, 22], 0, 4))
