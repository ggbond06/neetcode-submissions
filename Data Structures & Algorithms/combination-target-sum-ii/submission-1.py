class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        candidates.sort()


        def dfs(index, current, total):

            if total == target:
                copy = current[:]
                output.append(copy)
                return

            if total > target:
                return
            
            if index >= len(candidates):
                return
            
            current.append(candidates[index])
            total += candidates[index]
            dfs(index+1, current, total)
           

            current.pop()
            total -= candidates[index]

            next_index = index + 1

            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1

            dfs(next_index, current, total)

        
        dfs(0, [], 0)

        return output



            