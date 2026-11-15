import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones[:]
        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            y = heapq.heappop_max(max_heap)
            x = heapq.heappop_max(max_heap)
            if y == x:
                continue
            
            heapq.heappush_max(max_heap, y-x)

        return max_heap[0] if len(max_heap)>0 else 0
