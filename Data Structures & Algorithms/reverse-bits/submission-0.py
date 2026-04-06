class Solution:
    def reverseBits(self, n: int) -> int:
        new_n = 0
        for i in range(32):
            next_bit = 0
            if n & 1 == 1:
                next_bit = 1 
            next_bit = next_bit << (31 - i)
            new_n = new_n + next_bit
            n = n >> 1
        return new_n
        