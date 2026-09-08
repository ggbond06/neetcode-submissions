class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)

        for i,n in enumerate(nums):
            if i+1 == k:
                return n