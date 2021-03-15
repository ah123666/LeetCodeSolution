class Solution:
    def findNum(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1


s = Solution()
nums = [1, 4, 6, 7, 9, 13, 23, 45]
target = 1
print(s.findNum(nums, target))