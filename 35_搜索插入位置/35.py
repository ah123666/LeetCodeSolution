class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # nums.append(target)
        # nums.sort()
        # return nums.index(target)

        if nums is None or len(nums) == 0:
            return 0

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m + 1

        if nums[l] >= target:
            return l
        else:
            return l + 1
