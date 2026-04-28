class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        count = 0
        visited = set()
        def dfs(r, c) -> int:
            if min(r,c) < 0 or r == ROW or c == COL or (r,c) in visited or grid[r][c] == 1:
                return 0
            if r == ROW-1 and c == COL-1:
                return 1
            visited.add((r,c))
            count = 0
            count += dfs(r-1,c)
            count += dfs(r+1,c)
            count += dfs(r,c-1)
            count += dfs(r,c+1)
            visited.remove((r,c))
            return count
        return dfs(0,0)