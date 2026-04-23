class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(-1, -1) # dummy head node
        self.tail = Node(-1, -1) # dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, key, val):
        new_node = Node(key, val)
        self.tail.prev.next = new_node
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev = new_node
        return new_node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def insert_same_node_at_tail(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get_least_used_node(self):
        return self.head.next

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.dll = DoubleLinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if self.lru.get(key, -1) != -1:
            node = self.lru[key]
            self.dll.insert_same_node_at_tail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru[key].value = value
            self.dll.insert_same_node_at_tail(self.lru[key])
        else:
            if len(self.lru) == self.capacity:
                node = self.dll.get_least_used_node()
                self.dll.remove(node)
                del self.lru[node.key]
            new_node = self.dll.append(key, value)
            self.lru[key] = new_node