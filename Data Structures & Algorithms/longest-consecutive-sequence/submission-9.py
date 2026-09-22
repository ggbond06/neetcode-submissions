class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums_set = set(nums)

        compare = []

        for num in nums_set:
            if num - 1 not in nums_set:
                start = num
                count = 0
                count += 1
                while num + 1 in nums_set:
                    num += 1
                    count += 1
            
                compare.append(count)

        return max(compare)

             
        

            