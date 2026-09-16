class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        q = deque()

        visited = {}

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (
                    r == 0
                    or r == len(board) - 1
                    or c == 0
                    or c == len(board[0]) - 1
                ):
                    q.append((r,c))
                    visited[(r,c)] = True
                    
                    

        while q:

            r,c = q.popleft()

            directions = [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1),
            ]

            for dr, dc in directions:

                next_r = dr + r
                next_c = dc + c

                if next_r < 0 or next_c < 0 or next_r >= len(board) or next_c >= len(board[0]):
                    continue 

                if (next_r, next_c) in visited:
                    continue

                if board[next_r][next_c] == 'O':
                    visited[(next_r, next_c)] = True
                    q.append((next_r, next_c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'

                

