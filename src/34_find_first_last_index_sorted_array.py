from typing import List, Optional

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_left(A, target):
            l, r = 0, len(A) - 1
            while l <= r:
                mid = (l + r) // 2
                if A[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def search_right(A, target):
            l, r = 0, len(A) - 1
            while l <= r:
                mid = (l + r) // 2
                if A[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        l, r = search_left(nums, target), search_right(nums, target)

        return (l, r) if l <= r else (-1, -1)

