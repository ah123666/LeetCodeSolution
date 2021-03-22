from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        res = len(nums) + 1
        total = 0
        i = 0
        j = 0
        while j < len(nums):
            total += nums[j]
            j += 1
            while total >= target:
                res = min(res, j - i)
                total -= nums[i]
                i += 1

        if res == len(nums) - 1:
            return 0
        else:
            return res

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        size = 1
        while size <= len(nums):
            for i in range(len(nums) - size):
                total = sum(nums[i: i + size])
                if total >= target:
                    return size
            size += 1

        return 0
