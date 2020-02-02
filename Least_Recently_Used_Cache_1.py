import collections
class LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.ts =  time.time()
        self.next =  None
class LRU_Cache:
    def __init__(self, initial_size):
        if initial_size < 1:
            raise ValueError('Please enter a valid initial size')
        self.cache = collections.OrderedDict()
        self.cache_size = 0
        self.max_size = initial_size
    
    def size(self):
        return self.cache_size
    
    def set(self, key, value):
        if key:
            if len(self.cache) == self.max_size:
                # print("cache full")
                first_record = next(iter(self.cache))
                del self.cache[first_record]
                self.cache_size -= 1
            self.cache[key] = value
            self.cache_size += 1

    def get(self,key= None):
        if key:
            if key in self.cache:
                value = self.cache[key]
                del self.cache[key]  #deleting and inserting it again to move it up in the cache
                self.set(key, value)
                return self.cache[key]
        return -1

def test1():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print("Pass" if our_cache.get(1)== 1 else "Fail")      # returns 1
    print("Pass" if our_cache.get(2) == 2 else "Fail")      # returns 2
    print("Pass" if our_cache.get(9) == -1 else "Fail")      # edge case returns -1 because 9 is not present in the cache
    our_cache.set(5, 5) 
    our_cache.set(6, 6)
    print("Pass" if our_cache.get(3) == -1 else "Fail")      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry 
    

test1()

def test2(): #edge case when cache size is 0 or -1
    try:
        our_cache = LRU_Cache(0)
    except ValueError as err:
        print("Pass")

test2()

def test3():
    # print("Pass" if our_cache.get() == -1 else "Fail")   #edge case when key is not provided