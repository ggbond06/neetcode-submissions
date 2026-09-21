class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for start_r in range(0, 9, 3):
            for start_c in range(0, 9, 3):
                visited = set()
                for r in range(start_r, start_r +3):
                    for c in range(start_c, start_c + 3):

                        if board[r][c] == ".":
                            continue

                        if board[r][c] in visited:
                            return False

                        visited.add(board[r][c])

        for r in range(9):
            visited = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in visited:
                    return False
                visited.add(board[r][c])

        for c in range(9):
            visited = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in visited:
                    return False
                visited.add(board[r][c])

        return True

        

                 

