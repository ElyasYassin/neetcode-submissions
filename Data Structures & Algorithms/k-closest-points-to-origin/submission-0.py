from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points: 
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        
        i = 0
        while i < k:
            closest = heapq.heappop(minHeap) 
            res.append(closest[1:3])
            i += 1
        
        return res