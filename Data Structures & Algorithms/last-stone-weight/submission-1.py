class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:

            stones.sort()

            last = stones[-1]
            second_last = stones[-2]

            if last == second_last:
                stones.pop()
                stones.pop()
                stones.append(0)
            
            if last > second_last:
                stones.pop()
                stones.pop()
                stones.append(last - second_last)

        return stones[0]
