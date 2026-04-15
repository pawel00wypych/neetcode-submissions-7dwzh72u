class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)

        i = len(self.heap)-1
        while i // 2 > 0:
            if self.heap[i // 2] > self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i // 2]
                self.heap[i // 2] = tmp
                i = i // 2
            else:
                break

    def pop(self) -> int:
        if len(self.heap) < 2:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while i * 2 < len(self.heap):
            if i * 2 + 1 < len(self.heap) and  self.heap[i * 2] > self.heap[i * 2 + 1] and self.heap[i * 2 + 1] < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = tmp
                i = i * 2 + 1
            elif self.heap[i * 2] < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2]
                self.heap[i * 2] = tmp
                i = i * 2
            else:
                break
        return res

    def top(self) -> int:
        if len(self.heap) < 2:
            return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            return None
        if len(nums) == 1:
            self.heap.append(nums[0])
            return None

        self.heap = nums
        self.heap.append(nums[0])
        self.heap[0] = 0

        cur = (len(self.heap) - 1) // 2 # dont check leaves
        while cur > 0:
            i = cur
            while i * 2 < len(self.heap):
                if i * 2 + 1 < len(self.heap) and  self.heap[i * 2] > self.heap[i * 2 + 1] and self.heap[i * 2 + 1] < self.heap[i]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i * 2 + 1]
                    self.heap[i * 2 + 1] = tmp
                    i = i * 2 + 1
                elif self.heap[i * 2] < self.heap[i]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[i * 2]
                    self.heap[i * 2] = tmp
                    i = i * 2
                else:
                    break

            cur -= 1

        