class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0

        count1 = {}
        count2 = {}

        s1_len = len(s1)
        for char1 in range(s1_len):
            count1[s1[char1]] = count1.get(s1[char1], 0) + 1

        for right in range(len(s2)):
            count2[s2[right]] = count2.get(s2[right], 0) + 1

            if (right - left + 1) > s1_len:
                count2[s2[left]] -= 1
                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left += 1

            if (right - left + 1) == s1_len:
                if count1 == count2:
                    return True

        return False