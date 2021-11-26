from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return
        nums.sort()
        res = []
        for i, item in enumerate(nums[:-2]):
            if item > 0:
                break

            if i > 0 and item == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = item + nums[j] + nums[k]

                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    res.append([item, nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    assert [[-1,-1,2],[-1,0,1]] == Solution().threeSum(nums)
    nums = [1,-1,-1,0]
    assert [[-1,0,1]] == Solution().threeSum(nums)
