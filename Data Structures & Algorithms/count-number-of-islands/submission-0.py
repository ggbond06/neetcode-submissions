class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()

        def dfs(r,c):

            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return

            char = grid[r][c]
            
            if char == "0":
                return

            if (r,c) in visited:
                return
                
            visited.add((r,c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    total += 1
                    dfs(r,c)

        return total

            
