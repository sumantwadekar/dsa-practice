# Move all 0s to end

def move_0_to_end(arr):
    size = len(arr)
    first = 0
    last = size - 1
    while(first <= last):
        if arr[first] == 0:
            arr[first], arr[last] = arr[last], arr[first]
            last -= 1
        else:
            first += 1
    return arr

def remove_duplicates_from_sorted_array(arr):
    ''' Return count of unique elements in array '''
    size = len(arr)
    if size == 1:
        return 1
    index = 1
    repeatIndex = 1
    key = arr[index]
    while (index < size):
        if arr[index] != key:
            key = arr[index]
            arr[repeatIndex], arr[index] = arr[index], arr[repeatIndex]
            repeatIndex += 1
        index += 1
    return repeatIndex

def count_max_consecutive_1(arr):
    count = globalc = 0
    size = len(arr)
    index = 0
    while index < size:
        if arr[index] == 1:
            count += 1
        else:
            if count > globalc:
                globalc = count
            count = 0
        index += 1
    return globalc

# print(move_0_to_end([1, 0, 2, 3, 2, 0, 0, 4, 5, 1]))
print(remove_duplicates_from_sorted_array([1,1,2,2,2,3,3]))
# print(count_max_consecutive_1([1,1,2,2,2,1, 1, 1,3,3]))
