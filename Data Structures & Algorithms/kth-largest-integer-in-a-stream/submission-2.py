class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k + 1:
            self.heapPush(val)
        else:
            root_val = self.heapPop()
            if val > root_val:
                self.heapPush(val)
            else:
                self.heapPush(root_val)

        return self.heap[1]

    def heapPush(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

    def heapPop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while i * 2 < len(self.heap):
            if (i * 2 + 1) < len(self.heap) and  self.heap[i * 2 + 1] < self.heap[i * 2] and self.heap[i * 2 + 1] < self.heap[i]:
                # swap with right child
                tmp = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = self.heap[i]
                self.heap[i] = tmp
                i = i * 2 + 1
            elif self.heap[i * 2] < self.heap[i]:
                # swap with left child
                tmp = self.heap[i * 2]
                self.heap[i * 2] = self.heap[i]
                self.heap[i] = tmp
                i = i * 2
            else:
                # node is in the right place
                break
        return res
