class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s = {}
        map_t = {}
        
        for char in s:
            if char not in map_s:
                map_s[char] = 1
            else:
                map_s[char] += 1

        for char in t:
            if char not in map_t:
                map_t[char] = 1
            else:
                map_t[char] += 1
        
        if map_s != map_t:
            return False
        else:
            return True