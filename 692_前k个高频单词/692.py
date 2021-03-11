import heapq

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, nxt):
        return self.key > nxt.key if self.value == nxt.value\
            else self.value < nxt.value


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapping = {}
        for word in words:
            if word not in mapping:
                mapping[word] = 0
            mapping[word] = mapping[word] + 1

        heap = []
        for key, value in mapping.items():
            heapq.heappush(heap, Node(key, value))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while len(heap) > 0:
            temp = heapq.heappop(heap)
            res.append(temp.key)
        res.reverse()

        return res