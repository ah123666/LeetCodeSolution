class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s is None or len(s) == 0:
            return
        left = 0
        right = len(s) - 1
        self.recursion(s, left, right)

    def recursion(self, s, left, right):
        if left >= right:
            return
        return self.recursion(s, left+1, right-1)
        temp = s[left]
        s[left] = s[right]
        s[right] = temp