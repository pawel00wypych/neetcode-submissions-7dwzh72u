class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        print(stones)
        self.heapify(stones)
        
        while len(stones) > 2:
            print(stones)
            if len(stones) >= 4: # at least 2 children
                max_child_indx = 3 if stones[2] < stones[3] else 2
            elif len(stones) == 3: # 1 child
                max_child_indx = 2
            new_weight = stones[1] - stones[max_child_indx]
            self.pop_heap(stones)
            self.pop_heap(stones)

            if new_weight != 0:
                self.push_heap(stones, new_weight)
        
        return stones[1] if len(stones) == 2 else 0

    def heapify(self, arr: List[int]):
        if not arr:
            return
        if len(arr) == 1:
            arr.append(arr[0])
            arr[0] = 0
            return

        arr.append(arr[0])
        arr[0] = 0
        cur = (len(arr)-1) // 2
        while cur > 0:
            i = cur
            while i * 2 < len(arr):
                if (i * 2 + 1) < len(arr) and arr[i * 2 + 1] > arr[i * 2] and arr[i * 2 + 1] > arr[i]:
                    tmp = arr[i]
                    arr[i] = arr[i * 2 + 1]
                    arr[i * 2 + 1] = tmp
                    i = i * 2 + 1
                elif arr[i * 2] > arr[i]:
                    tmp = arr[i]
                    arr[i] = arr[i * 2]
                    arr[i * 2] = tmp
                    i = i * 2
                else:
                    break
            cur -= 1
        return

    def pop_heap(self, arr):
        if len(arr) < 2:
            return
        if len(arr) == 2:
            arr.pop()
            return
        arr[1] = arr.pop()

        i = 1
        while i * 2 < len(arr):
                if (i * 2 + 1) < len(arr) and arr[i * 2 + 1] > arr[i * 2] and arr[i * 2 + 1] > arr[i]:
                    tmp = arr[i]
                    arr[i] = arr[i * 2 + 1]
                    arr[i * 2 + 1] = tmp
                    i = i * 2 + 1
                elif arr[i * 2] > arr[i]:
                    tmp = arr[i]
                    arr[i] = arr[i * 2]
                    arr[i * 2] = tmp
                    i = i * 2
                else:
                    break

    def push_heap(self, arr, val):

        arr.append(val)
        i = len(arr) - 1
        while i // 2 > 0:
            if arr[i] > arr[i // 2]:
                tmp = arr[i]
                arr[i] = arr[i // 2]
                arr[i // 2] = tmp
                i = i // 2
            else:
                break