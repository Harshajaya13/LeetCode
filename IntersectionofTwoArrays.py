from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = set(nums2)
        result = set()
        for x in nums1:
            if x in nums2:
                result.add(x)
        return list(result)

