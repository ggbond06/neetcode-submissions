class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 0:
                    q.append((row,column,0))

        while q:
            r,c,d = q.popleft()

            directions = [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1),
            ]

            for dr, dc in directions:

                next_r = r + dr
                next_c = c + dc

                if next_r >= len(grid) or next_c >= len(grid[0]) or next_r < 0 or next_c < 0:
                    continue
                
                if grid[next_r][next_c] == 2147483647:
                    grid[next_r][next_c] = d+1

                    q.append((next_r, next_c, d+1))
                
                

