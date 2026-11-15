class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            dist = x**2 + y**2
            if len(heap) < k:
                heapq.heappush_max(heap, (dist, [x,y]))
                continue
            
            if dist < heap[0][0]:
                heapq.heapreplace_max(heap, (dist, [x,y]))
        
        return [point for dist, point in heap]
