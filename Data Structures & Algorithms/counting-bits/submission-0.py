class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def bitsInInteger(num: int) -> int:
            count = 0
            while num > 0:
                if num & 1 == 1:
                    count += 1
                num = num >> 1
            return count

        for i in range(n+1):
            res.append(bitsInInteger(i))
        return res
