from typing import List, Optional

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        Solution.dfs(candidates, target, [], ret)
        return ret

    @staticmethod
    def dfs(nums: List[int], target: int, path: List[int], ret: List[List[int]]):
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            if target < nums[i]:
                break
            Solution.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)