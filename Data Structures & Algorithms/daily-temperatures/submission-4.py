class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            n = temperatures[i]
            start_day = i + 1

            while start_day < len(temperatures):
                if temperatures[start_day] > n:
                    result[i] = start_day - i
                    break
                
                if result[start_day] == 0:
                    break

                start_day += result[start_day]

        return result
