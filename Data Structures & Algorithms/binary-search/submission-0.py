class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i_low = 0
        i_high = len(nums) - 1

        while i_low <= i_high:
            i_middle = (i_low + i_high) // 2
            if target == nums[i_middle] :
                return i_middle

            elif target < nums[i_middle] :
                i_high = i_middle - 1
            else:
                i_low = i_middle + 1

        return -1
        