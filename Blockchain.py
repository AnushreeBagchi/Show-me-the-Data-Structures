import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None
    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = "We are going to encode this string of data!".encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.no_blocks = 0

    def append(self, data):
        if self.head is None:
            previous_hash = None
            self.head = Block(time.time(), data, previous_hash)
            self.tail = self.head
        else:
            previous_hash = self.tail.hash
            self.tail.next = Block(time.time(), data, previous_hash)
            self.tail = self.tail.next
        self.no_blocks += 1
    
    def size(self):
        return self.no_blocks

    

data1 = "Data for first block"
data2 = "Data for second block"
data3 = "Data for third block"

linkedlist = LinkedList()
linkedlist.append(data1)
linkedlist.append(data2)
linkedlist.append(data3)

def test(ll):
    node = ll.head
    while node.next:
        if node.hash != node.next.previous_hash:
            return "Test Failed"
        node = node.next
    return "Test Passed"

print(test(linkedlist))
print(linkedlist.size())
