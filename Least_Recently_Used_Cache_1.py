import collections
class LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.ts =  time.time()
        self.next =  None
class LRU_Cache:
    def __init__(self, initial_size=5):
        self.cache = collections.OrderedDict()
        self.cache_size = 0
        self.max_size = initial_size
    
    def size(self):
        return self.cache_size
    
    def set(self, key, value):
        if len(self.cache) == self.max_size:
            # print("cache full")
            first_record = next(iter(self.cache))
            del self.cache[first_record]
            self.cache_size -= 1
        self.cache[key] = value
        self.cache_size += 1

    def get(self,key):
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]  #deleting and inserting it again to move it up in the cache
            self.set(key, value)
            return self.cache[key]
        return -1
       
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

# print(our_cache)

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry