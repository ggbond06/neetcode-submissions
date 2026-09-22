class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        visited = {}
        output = []

        for word in strs:
            key = tuple(sorted(word))
            if key not in visited:
                visited[key] = [word]
            else:
                visited[key].append(word)

        for key, value in visited.items():
            output.append(value)

        return output