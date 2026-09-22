class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)

        end = 0

        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
            
        count = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * count
            count *= nums[i]

        return output
