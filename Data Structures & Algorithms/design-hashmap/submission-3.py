class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyHashMap:

    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.table = [None] * self.capacity

    def put(self, key: int, value: int) -> None:
        hash_ind = self.hash(key)

        while self.table[hash_ind] is not None:
            if self.table[hash_ind].key == key:
                self.table[hash_ind] = Pair(key, value)
                return
            hash_ind = (hash_ind + 1) % self.capacity

        self.size += 1
        self.table[hash_ind] = Pair(key, value)
        if self.size >= self.capacity // 2:
            self.resize()

    def get(self, key: int) -> int:
        hash_ind = self.hash(key)
        while self.table[hash_ind] is not None:
            if self.table[hash_ind].key == key:
                return self.table[hash_ind].val
            hash_ind = (hash_ind + 1) % self.capacity
        return -1

    def remove(self, key: int) -> None:
        hash_ind = self.hash(key)
        while self.table[hash_ind] is not None:
            if self.table[hash_ind].key == key:
                self.table[hash_ind] = None
                nxt_ind = (hash_ind + 1) % self.capacity
                nxt_pair = self.table[nxt_ind]

                while nxt_pair is not None:
                    self.table[nxt_ind] = None
                    self.size -= 1
                    self.put(nxt_pair.key, nxt_pair.val)
                    nxt_ind = (nxt_ind + 1) % self.capacity
                    nxt_pair = self.table[nxt_ind]
                return
            hash_ind = (hash_ind + 1) % self.capacity
        

    def hash(self, key):
        return key % self.capacity

    def resize(self):
        old_t = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0
        for p in old_t:
            if p is not None:
                self.put(p.key, p.val)
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)