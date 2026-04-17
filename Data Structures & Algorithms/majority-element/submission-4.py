class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        def majorityElementHelper(l, r):
            if l == r:
                return nums[l]

            left_most = majorityElementHelper(l, (l+r) // 2)
            right_most = majorityElementHelper((l + r) // 2 + 1,r)

            if left_most == right_most:
                return left_most

            left_count = sum(1 for i in range(l, r + 1) if nums[i] == left_most)
            right_count = sum(1 for i in range(l, r + 1) if nums[i] == right_most)

            return left_most if left_count > right_count else right_most
        res =  majorityElementHelper(0, len(nums)-1)
        return res