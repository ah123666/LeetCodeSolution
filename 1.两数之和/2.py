# 哈希表
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0, 0]
        map = {}
        for i in range(0, len(nums)):
            map[nums[i]] = i

        print(map)

        for j in range(0, len(nums)):
            diff = target - nums[j]
            if diff in map and map[diff] != j:
                result[0] = j
                result[1] = map[diff]
                return result
        return result



if __name__ == '__main__':
    s = Solution()
    nums = [11, 15, 2, 7]
    target = 9
    print(s.twoSum(nums, target))