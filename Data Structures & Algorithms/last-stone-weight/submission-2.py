import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if y == x:
                continue
            
            else:
                heapq.heappush(max_heap, -(y-x))
        
        return -max_heap[0] if len(max_heap) > 0 else 0
