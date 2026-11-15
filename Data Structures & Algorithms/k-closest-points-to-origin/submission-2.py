class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush_max(heap, (dist, point))
        
        while len(heap) > k:
            heapq.heappop_max(heap)
        
        ans = []

        while heap:
            dist, point = heapq.heappop_max(heap)
            ans.append(point)
        
        return ans