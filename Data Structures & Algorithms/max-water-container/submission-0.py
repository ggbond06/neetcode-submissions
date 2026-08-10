class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1

        max_area = 0

        while start < end:
            if heights[start] <= heights[end]:
                temp = (end - start) * heights[start]
                if temp > max_area:
                    max_area = temp
                start+=1
            elif heights[start] > heights[end]:
                temp = (end - start) * heights[end]
                if temp > max_area:
                    max_area = temp
                end-=1


        return max_area

        