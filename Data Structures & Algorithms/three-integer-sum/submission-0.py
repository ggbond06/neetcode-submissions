class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list_new = []
        nums.sort()
        for i, n in enumerate(nums):
            start = i + 1
            end = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while start < end:
                total = n + nums[start] + nums[end]
                if total == 0:
                    list_new.append([n, nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                elif total < 0:
                    start += 1
                else:
                    end -= 1

        return list_new