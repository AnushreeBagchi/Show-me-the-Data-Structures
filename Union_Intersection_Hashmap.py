class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
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
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
    def to_list(self):
        py_list = []
        node = self.head
        while node:
            py_list.append(node.value)
            node = node.next
        return py_list

class HashMap:
    def __init__(self):
        self.map = dict()
        self.size = 0
    def set(self, key):
        if key in self.map:
            self.map[key].value += 1
        else:
            self.map[key] = 1
    def get(self,key):
        if key in self.map:
            return self.map[key]
        return None

def union(llist_1=None, llist_2=None):
    if llist_1 == None and llist_2 == None:
        return None
    elif llist_1 == None:
        return llist_2
    elif llist_2 == None:
        return llist_1
    else:
        hashmap = HashMap()
        result_ll = LinkedList()
        node = llist_1.head
        while node is not None:
            if not hashmap.get(node.value):
                hashmap.set(node.value)
                result_ll.append(node.value)
            node = node.next
        node = llist_2.head
        while node:
            if not hashmap.get(node.value):
                hashmap.set(node.value)
                result_ll.append(node.value)
            node = node.next
        return result_ll

def intersection(llist_1=None, llist_2=None):
    if llist_1 == None and llist_2 == None:
        return None
    elif llist_1 == None or llist_2 == None:
        return LinkedList()
    else:
        hashmap = HashMap()
        hashmap2 = HashMap() #to avod duplicates
        result_ll = LinkedList()
        node = llist_1.head
        while node:
            if not hashmap.get(node.value):
                hashmap.set(node.value)
            node = node.next
        node = llist_2.head
        while node:
            if hashmap.get(node.value) and not hashmap2.get(node.value):
                hashmap2.set(node.value)
                result_ll.append(node.value)
            node = node.next
        return result_ll

# Test case 1
def test1():
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
    print("Pass" if union_result.to_list()== [3,2,4,35,6,65,21,32,9,1,11] else "Fail")
    print("Pass" if intersection_result.to_list() == [6,4,21] else "Fail")
test1()

# Test case 2
def test2():
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()
    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]
    for i in element_1:
        linked_list_3.append(i)
    for i in element_2:
        linked_list_4.append(i)
    print ("Pass" if union(linked_list_3,linked_list_4).to_list() == [3,2,4,35,6,65,23,1,7,8,9,11,21] else "Fail")
    print ("Pass" if intersection(linked_list_3,linked_list_4).to_list() == [] else "Fail")
test2()

#edge case when both the linkedlist do not have any nodes
def test3(): 
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()
    element_1 = []
    element_2 = []
    for i in element_1:
        linked_list_3.append(i)
    for i in element_2:
        linked_list_4.append(i)
    print ("Pass" if union(linked_list_3,linked_list_4).to_list() == [] else "Fail")
    print ("Pass" if intersection(linked_list_3,linked_list_4).to_list() == [] else "Fail")
test3()

#edge case when only one linkedlist is present
def test4(): 
    linked_list_3 = LinkedList()
    element_1 = [1,2,3]
    for i in element_1:
        linked_list_3.append(i)
   
    print ("Pass" if union(linked_list_3).to_list() == [1,2,3] else "Fail")
    print ("Pass" if intersection(linked_list_3).to_list() == [] else "Fail")
test4()