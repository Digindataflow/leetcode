from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            return
        nums.sort()
        min_sum = nums[0] + nums[1] + nums[2] - target
        for i, item in enumerate(nums[:-2]):
            if item > target:
                break

            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = item + nums[j] + nums[k] - target
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    return target

                min_sum = min(min_sum, s, key=abs)
        return min_sum + target

if __name__ == "__main__":
    nums = [1,2,5,10,11]
    target = 13
    assert 13 == Solution().threeSumClosest(nums, target)