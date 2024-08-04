"""
Stack implementation using lists
"""

class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.top = -1

    def put(self, value):
        self.stack.append(value)
        self.top = value

    def pop(self):
        try:
            stack_top = self.stack.pop()
            self.top = stack_top
            return stack_top
        except Exception:
            print('Stack already empty')

    def __str__(self) -> str:
        # Display the stack in array format
        return str(self.stack)


if __name__ == '__main__':
    stc = Stack()
    stc.put(1)
    stc.put(2)
    stc.put(3)
    stc.put(4)
    stc.pop()
    print('scw')

    # Using python libraries
    from collections import deque

    # stc = deque()
    # stc.append(1)
    # stc.append(2)
    # stc.append(3)
    # print(stc)
    # stc.pop()
    # stc.pop()
    # print(stc)
