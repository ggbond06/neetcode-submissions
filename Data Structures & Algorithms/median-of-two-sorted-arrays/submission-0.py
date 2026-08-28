class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        merged = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        
        if (len(merged) % 2) ==  0:
            upper = int(len(merged) / 2)
            lower = upper - 1
            sum = merged[upper] + merged[lower]
            return float(sum / 2)
        else:
            mid = (len(merged) - 1) // 2
            return float(merged[mid])

