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
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        for num in nums2:
            stack.append(num)

        for num in nums1:
            temp = []
            isFond = False
            max = -1
            while len(stack) != 0 and not isFond:
                top = stack.pop()
                if top > num:
                    max = top
                elif top == num:
                    isFond = True
                temp.append(top)
            res.append(max)
            while len(temp) != 0:
                stack.append(temp.pop())
        return res
        
