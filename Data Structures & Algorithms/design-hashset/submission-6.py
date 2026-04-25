class MyHashSet:

    def __init__(self):
        self.hash_set = [None, None]
        self.capacity = 2
        self.size = 0

    def add(self, key: int) -> None:
        hash_ind = self.hash(key)
        while self.hash_set[hash_ind] is not None:
            if self.hash_set[hash_ind] == key:
                return
            hash_ind = (hash_ind + 1) % self.capacity
        self.hash_set[hash_ind] = key
        self.size += 1
        if self.size >= self.capacity // 2:
            self.resize()

    def remove(self, key: int) -> None:
        hash_ind = self.hash(key)
        while self.hash_set[hash_ind] is not None:
            if self.hash_set[hash_ind] == key:
                self.hash_set[hash_ind] = None
                self.size -= 1
                # prevent from bugs when there is a hole between keys with the same hash
                while self.hash_set[(hash_ind + 1) % self.capacity] is not None: 
                    val = self.hash_set[(hash_ind + 1) % self.capacity]
                    self.hash_set[(hash_ind + 1) % self.capacity] = None
                    self.size -= 1
                    self.add(val)
                    hash_ind = (hash_ind + 1) % self.capacity
                return
            hash_ind = (hash_ind + 1) % self.capacity
        

    def contains(self, key: int) -> bool:
        hash_ind = self.hash(key)
        while self.hash_set[hash_ind] is not None:
            if self.hash_set[hash_ind] == key:
                return True
            hash_ind = (hash_ind + 1) % self.capacity
        return False

    def hash(self, key) -> int:
        return key % self.capacity

    def resize(self):
        old_h_set = self.hash_set
        self.capacity *= 2
        self.hash_set = [None] * self.capacity
        self.size = 0
        for k in old_h_set:
            if k is not None:
                self.add(k)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)