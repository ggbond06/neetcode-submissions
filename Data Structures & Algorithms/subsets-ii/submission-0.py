class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        def dfs(index, current):
            if index >= len(nums):
                
                copy = current[:]
                output.append(copy)
                return

            current.append(nums[index])
            dfs(index+1, current)

            current.pop()
            next_index = index+1
            while next_index < len(nums) and nums[next_index] == nums[index]:
                next_index += 1
            dfs(next_index, current)

        dfs(0,[])

        return output