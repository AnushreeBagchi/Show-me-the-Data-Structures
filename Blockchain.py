import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (self.data + str(self.timestamp)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.no_blocks = 0

    def append(self, data):
        if self.head is None:
            previous_hash = None
            self.head = Block(datetime.now(), data, previous_hash)
            self.tail = self.head
        else:
            previous_hash = self.tail.hash
            self.tail.next = Block(datetime.now(), data, previous_hash)
            self.tail = self.tail.next
        self.no_blocks += 1
    
    def size(self):
        return self.no_blocks

def printDetails(node):
    if node is None:
        raise ValueError('Please enter a valid group')
    else:
        print("Timestamp: {}".format(node.timestamp))
        print("Data: {}".format(node.data))
        print("Hash: {}".format(node.hash))
        print("previous Hash: {}".format(node.previous_hash))
        print("\n")


def test1():
    print("Test1--------------------------------------")
    data1 = "Data for first block"
    data2 = "Data for second block"
    data3 = "Data for third block"

    blockchain = Blockchain()
    blockchain.append(data1)
    blockchain.append(data2)
    blockchain.append(data3)
    node = blockchain.head
    if node.hash!= node.next.previous_hash:
            return "Test Failed"
    while node:
        printDetails(node)        
        node = node.next
    return "Test Passed"

def test2(): #edge case with just one block
    print("Test2--------------------------------------")
    data1 = ""
    blockchain = Blockchain()
    blockchain.append(data1)
    node = blockchain.head
    printDetails(node)
    if node.next == None and node.hash != None:
        return "Test Passed"
    else:
        return "Test Failed"

def test3():  #edge case with no data
    print("Test3 -------------------------------------")
    blockchain = Blockchain()
    node = blockchain.head
    try:
        printDetails(node)
    except ValueError as err:
        return "Test Passed"
        
print(test1())
print(test2())
print(test3())

