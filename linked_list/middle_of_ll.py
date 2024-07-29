from linked_list_impl import Node

class LinkedListMiddleNodeOp():
    # def __init__(self, head: Node) -> None:
    #     self.head = head

    def middle_of_linked_list(self, head) -> int:
        # Here we will use slow pointer and fast pointer
        # Define two variables pointed to head of linked list, and after each iteration
        # move slow pointer by one node and fast pointer by two nodes
        slow_ptr = fast_ptr = head
        while(fast_ptr and fast_ptr.next != None):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr.data

    def delete_middle_node(self, head: Node) -> None:
        # here we need again two pointers to find middle of linked list
        # but also require an additional third pointer to track the prev node of middle node to enable deletion
        # handle base cases first
        if head.next == None:
            return None
        prev_mid_node = slow_ptr = fast_ptr = head
        while(fast_ptr and fast_ptr.next != None):
            prev_mid_node = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        prev_mid_node.next = slow_ptr.next
        return head


head = Node(2)
head = head.add_to_head(1)
head = head.add_to_tail(3)
head = head.add_to_tail(4)
# It is not compulsory to add init func to class
ops = LinkedListMiddleNodeOp()
head = ops.delete_middle_node(head)
print(head)
