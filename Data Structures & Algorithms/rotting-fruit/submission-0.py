class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()

        time = 0
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        while q:

            if fresh == 0:
                break

            size = len(q)

            for i in range(size):
                r, c = q.popleft()

                directions = [
                    (1,0),
                    (-1,0),
                    (0,1),
                    (0,-1),
                ]

                for dr, dc in directions:

                    next_r = r + dr
                    next_c = c + dc

                    if next_r < 0 or next_c < 0 or next_r >= len(grid) or next_c >= len(grid[0]):
                        continue

                    if grid[next_r][next_c] == 1:
                        grid[next_r][next_c] = 2
                        q.append((next_r,next_c))
                        fresh -= 1
                        
                    else:
                        continue

            time += 1

        if fresh != 0:
            return -1

        return time

