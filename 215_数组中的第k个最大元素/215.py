import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for num in nums:
            heapq.heappush(minHeap, num)

        m = len(nums) - k
        while m >= 1:
            heapq.heappop(minHeap)
            m -= 1
        return heapq.heappop(minHeap)