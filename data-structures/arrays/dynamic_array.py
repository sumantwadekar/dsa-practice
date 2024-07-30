'''
Implement dynamic arrays using static array

1. Static arrays are fixed in length
2. Add/ Remove elements until sufficient capacity
3. If adding an element exceeds capacity, make length of static array twice
4. If removing an element makes the length of array less than 0, raise the error
5. Add methods for clearing/ deletion/ insertion/ Appending/ Searching
'''

class DynamicArray:
    def __init__(self, capacity) -> None:
        self.length = 0
        self.capacity = capacity
        self.arr = [-1] * capacity


    def set(self, index: int, value: int):
        if self.length == self.capacity:
            # time to resize
            self.resize()

        # Now add the element according to its target index
        # right shift the elements to accommodate the new element
        for item in range(self.length, index, -1):
            self.arr[item] = self.arr[item - 1]
        self.arr[index] = value
        self.length += 1

    def append(self, value: int):
        if self.length == self.capacity:
            # time to resize
            self.resize()
        self.arr[self.length] = value
        self.length += 1


    def remove(self, index: int):
        # check if array length is already 0
        if (self.length == 0) or (index >= self.length or index < 0):
            raise Exception('Array is empty already or invalid index provided')
        for item in range(index, self.length):
            self.arr[item] = self.arr[item + 1]

        self.length -= 1

    def get(self, index: int):
        return self.arr[index]

    def __str__(self) -> str:
        return f"[{','.join(self.arr)}]"


    def resize(self):
        if self.capacity == 0:
            self.capacity = 1
        else:
            self.capacity *= 2
        new_arr = [-1] * self.capacity
        for index in range(len(self.arr)):
            new_arr[index] = self.arr[index]
        self.arr = new_arr


if __name__ == '__main__':
    arr = DynamicArray(5)
    arr.set(0, 10)
    arr.set(1, 20)
    arr.set(2, 30)
    arr.set(3, 40)
    arr.set(4, 50)
    arr.set(9, 200)
    arr.set(0, 2000)
    arr.remove(2)
    print(str(arr))
