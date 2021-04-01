class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.getMajority(nums, 0, len(nums) - 1)

    def getMajority(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = left + (right - left) // 2
        leftMajority = self.getMajority(nums, left, mid)
        rightMajority = self.getMajority(nums, mid + 1, right)

        if leftMajority == rightMajority:
            return leftMajority

        leftCount = 0
        rightCount = 0
        for i in nums[left:right + 1]:
            if i == leftMajority:
                leftCount += 1
            elif i == rightMajority:
                rightCount += 1
        if leftCount > rightCount:
            return leftMajority
        else:
            return rightMajority



