from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None or len(nums) == 0:
            return 0

        l = 0
        r = len(nums) - 1
        while l < r:
            while l < r and nums[l] != val:
                l += 1
            while l < r and nums[r] == val:
                r -= 1
            temp = nums[r]
            nums[r] = nums[l]
            nums[l] = temp

        if nums[l] == val:
            return l
        else:
            return l + 1
