class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.length += 1
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        self.length += 1
    def appendNode (self, input_node):
        if self.head is None:
            self.head = input_node
            self.length += 1
            return
        node = self.head
        while node.next:
            node = node.next
        input_node.next = None
        node.next = input_node

    def size(self):
        return self.length

    def to_list(self):
        py_list = []
        node = self.head
        while node:
            py_list.append(node.value)
            node = node.next
        return py_list
    def is_value_present(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next

def intersection(llist_1, llist_2):
    # Your Solution Here
    result_ll = LinkedList()
    node1 = llist_1.head    
    while node1:
        node2 = llist_2.head
        while node2:
            if node1.value == node2.value:
                if not result_ll.is_value_present(node1.value):
                    result_ll.append(node1.value)
            node2=node2.next
        node1 = node1.next
    return result_ll

def union(llist_1, llist_2):
    # Your Solution Here
    result_ll = LinkedList()
    node1 = llist_1.head
    node2 = llist_2.head
    while node1:
        result_ll.append(node1.value)
        node1 = node1.next
    while node2:
        if not result_ll.is_value_present(node2.value):
            result_ll.append(node2.value)
        node2 = node2.next
    return result_ll
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


union_result = union(linked_list_1,linked_list_2)
intersection_result = intersection(linked_list_1,linked_list_2)
print("Pass" if union_result.to_list()== [3,2,4,35,6,65,6,4,3,21,32,9,1,11] else "Fail")
print("Pass" if intersection_result.to_list() == [4,6,21] else "Fail")

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

union_result = union(linked_list_3,linked_list_4)
intersection_result = intersection(linked_list_3,linked_list_4)

print("Pass" if union_result.to_list()== [3,2,4,35,6,65,6,4,3,23,1,7,8,9,11,21] else "Fail")
print("Pass" if intersection_result.to_list() == [] else "Fail")



