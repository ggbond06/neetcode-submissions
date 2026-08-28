class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}

        for num in nums:
            if num in myMap:
                myMap[num] += 1
            else:
                myMap[num] = 1


        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in myMap.items():
            buckets[frequency].append(num)

        result = []

        for frequency in range(len(buckets) - 1, 0, -1):
            for num in buckets[frequency]:
                result.append(num)

                if len(result) == k:
                    return result