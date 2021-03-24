class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if s is None or len(s) < k:
            return 0

        table = ['a', 'e', 'i', 'o', 'u']
        res = 0
        count = 0
        for i in range(0, k):
            if s[i] in table:
                count += 1
        res = count

        for i in range(k, len(s)):
            if s[i-k] in table:
                count -= 1
            if s[i] in table:
                count += 1
            if count > res:
                res = count
        return res
