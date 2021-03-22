# 暴力法
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0, 0]
        for i in range(0, len(nums) - 1):
            for j in range(i, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    result[0] = i
                    result[1] = j
                    return result
        return result


s = Solution()
nums = [11, 15, 2, 7]
target = 9

print(s.twoSum(nums, target))
