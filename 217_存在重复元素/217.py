class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0:
            return False
        hashMap = {}
        for num in nums:
            if num in hashMap:
                return True
            hashMap[num] = 1
        return False
