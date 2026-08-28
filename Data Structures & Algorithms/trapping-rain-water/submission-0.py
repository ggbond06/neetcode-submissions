class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]

        water = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
            else:
                right -= 1
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]

        return water