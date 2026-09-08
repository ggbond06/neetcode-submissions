class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        points.sort(key=lambda points: points[0]**2 + points[1]**2)

        return points[:k]


        