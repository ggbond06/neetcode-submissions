class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        output = []

        def dfs(index, current, total):

            if total == target:
                copy = current[:]
                output.append(copy)
                return

            if total > target:
                return
            
            if index >= len(nums):
                return


            total += nums[index]
            current.append(nums[index])
            dfs(index, current, total)

            current.pop()
            total -= nums[index]
            dfs(index+1, current, total)


        dfs(0, [], 0)

        return output
