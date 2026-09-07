class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()

        max_total = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 0

            char = grid[r][c]

            if (r,c) in visited:
                return 0

            if char == 0:
                return 0

            visited.add((r,c))

            area = 1

            area += dfs(r+1,c)
            area += dfs(r,c+1)
            area += dfs(r-1,c)
            area += dfs(r,c-1)

            return area
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited:
                    area = dfs(r,c)
                    max_total = max(max_total, area)


        return max_total
            