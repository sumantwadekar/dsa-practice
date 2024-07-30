"""
Linked list implementation
This node class will be used in different alogorithms associated with linked lists
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


    ''' Forward reference used in below definitions '''

    def add_to_head(self, data) -> 'Node':
        # create an instance of Node class to denote the new node
        new_node = Node(data)
        # Make the new node `Head` by assigning current head to next pointer of new node
        new_node.next = self
        return new_node


    def add_to_tail(self, data) -> 'Node':
        # create an instance of Node class to denote the new node
        new_node = Node(data)
        # Traverse the linked list to find out existing tail node
        temp_head = self
        # Continue loop until the node where next pointer is set to null
        while temp_head.next != None:
            temp_head = temp_head.next
        # Now temp_head points to tail node of linked list
        temp_head.next = new_node
        return self


    def add_element_at_index(self, index, data):
        # handle garbage input
        if index < 0:
            return self
        if index == 0:
            return self.add_to_head(data)

        # To add an element at specified index, we need to access the element at index - 1
        # So that we can set next pointer to new node and existing next pointer to next ptr of new node
        temp_head = self
        while(temp_head != None and ((index - 1) > 0)):
            temp_head = temp_head.next
            index -= 1
        # check if head set to null before reaching to particular index
        if not temp_head:
            print('Index greater than length of linked list')
            return self
        # create an instance of Node class to denote the new node
        new_node = Node(data)
        new_node.next = temp_head.next
        temp_head.next = new_node
        return self


    def remove_element_at_index(self, index):
        # If head node to be removed, just point head to its next node
        if index == 0:
            return self.next
        # To add an element at specified index, we need to access the element at index - 1
        # So that we can set next pointer to new node and existing next pointer to next ptr of new node
        temp_head = self
        while(temp_head != None and ((index - 1) > 0)):
            temp_head = temp_head.next
            index -= 1
        # check if head set to null before reaching to particular index
        if not temp_head:
            print('Index greater than length of linked list')
            return self
        temp_head.next = temp_head.next.next
        return self



    def __str__(self) -> str:
        # Display the linked list in array format
        response = '['
        temp_node = self
        while temp_node:
            response += (str(temp_node.data) + ', ')
            temp_node = temp_node.next
        response = (response[:-2] +  ']')
        return response


if __name__ == '__main__':
    head = Node(2)
    head = head.add_to_head(1)
    head = head.add_to_tail(3)
    head = head.add_to_tail(4)
    head = head.remove_element_at_index(0)
    print(head)
