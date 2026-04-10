class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = [[]]

        for n in nums:
            temp_solution = []
            for s in solution:
                n_list = [n] + s
                temp_solution.append(n_list)
            solution.extend(temp_solution)
        return solution