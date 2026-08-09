class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            sum = numbers[start] + numbers[end]
            temp_start = start
            temp_end = end
            if sum == target :
                temp_start += 1
                temp_end += 1
                return [temp_start, temp_end]

            elif sum < target:
                start+=1
            else:
                end-=1

        return -1