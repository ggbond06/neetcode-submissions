class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(index, current):

            if index >= len(nums):
                copy = current[:]
                output.append(copy)
                return
            
            current.append(nums[index])

            dfs(index+1, current)

            current.pop()

            dfs(index+1, current)

        
        dfs(0, [])

        return output