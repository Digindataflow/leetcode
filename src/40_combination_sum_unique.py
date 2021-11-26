from typing import List, Optional

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        Solution.dfs(candidates, 0, target, [], ret)
        return ret

    @staticmethod
    def dfs(nums: List[int], start: int, target: int, path: List[int], ret: List[List[int]]):
        if target == 0:
            ret.append(path)
            return
        for i in range(start, len(nums)):
            if target < nums[i]:
                break
            # only skip like start = 0, i = 1
            if i > start and nums[i] == nums[i-1]:
                continue
            Solution.dfs(nums, i+1, target-nums[i], path+[nums[i]], ret)