class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        count = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                result = max(result, count)
                count = 0

        return max(result, count)