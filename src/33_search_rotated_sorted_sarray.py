from typing import List, Optional

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            j = len(nums) - 1
            while j > 0 and nums[j-1] < nums[j]:
                if nums[j] == target:
                    return j
                j -= 1
            if nums[j] == target:
                return j
            else:
                return -1
        else:
            i = 0
            while i < len(nums) - 1 and nums[i] < nums[i+1]:
                if nums[i] == target:
                    return i
                i += 1

            if nums[i] == target:
                return i
            else:
                return -1