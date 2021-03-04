from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        temp_stack = []
        for item in nums2:
            stack.append(item)

        result = []
        for item1 in nums1:
            while stack[-1] != item1:
                temp = stack.pop()
                temp_stack.append(temp)
            get_result = False
            while len(temp_stack) > 0:
                temp = temp_stack.pop()
                stack.append(temp)
                if temp > item1 and not get_result:
                    result.append(temp)
                    get_result = True
            if not get_result:
                result.append(-1)
        return result

s = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
res = s.nextGreaterElement(nums1, nums2)
