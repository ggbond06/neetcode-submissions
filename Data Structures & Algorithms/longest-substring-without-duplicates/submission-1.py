class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        end = 0
        start = 0
        max = 0

        while end < len(s):
            current = s[end] 
            if current not in seen:
                seen.add(current)

                current_window_length = end - start + 1

                if current_window_length > max:
                    max = current_window_length

                end+=1

            else:
                seen.remove(s[start])
                start+=1

        return max