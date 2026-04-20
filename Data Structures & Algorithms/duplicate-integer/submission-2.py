class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for n in nums:
            duplicates[n] = duplicates.get(n, 0) + 1
            if duplicates[n] > 1:
                return True
        return False