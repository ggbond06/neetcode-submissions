class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) - 1

        while start <= end:
            mid = (end + start) // 2
            col = mid % len(matrix[0])
            row = mid // len(matrix[0])
            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                start+=1
            else:
                end-=1

        return False
