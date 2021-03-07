class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t

        hashTable = [0]*26
        for i in s:
            temp = ord(i) - 97
            hashTable[temp] -= 1
        for j in t:
            temp = ord(j) - 97
            hashTable[temp] += 1

        for k in range(26):
            if hashTable[k] == 1:
                asciiValue = k + 97
                return chr(asciiValue)
