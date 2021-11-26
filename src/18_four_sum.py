from typing import List

def find_nsum(nums: List[int], n: int, target: int, cur: List[int]):
    if len(nums) < n or n < 2:
        return
    nums.sort()
    res = []
    if n == 2:
        i = 0
        j = len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]

            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                res.append(cur + [nums[i], nums[j]])
                while i < j and nums[i] == nums[i+1]:
                    i += 1
                while i < j and nums[j] == nums[j-1]:
                    j -= 1
                i += 1
                j -= 1
    else:
        for k, item in enumerate(nums[:-(n-1)]):
            if k == 0 or item != nums[k-1]:
                res.extend(find_nsum(nums[k+1:], n-1, target-item, cur+[item]))
    return res

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    assert find_nsum(nums, 4, target, [])

    nums = [-1,0,-5,-2,-2,-4,0,1,-2]
    target = -9
    assert find_nsum(nums, 4, target, []) == [[-5,-4,-1,1],[-5,-4,0,0],[-5,-2,-2,0],[-4,-2,-2,-1]]

