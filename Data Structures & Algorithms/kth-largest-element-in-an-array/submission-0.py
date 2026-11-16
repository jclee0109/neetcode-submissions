class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max heap (heapify, pop) vs min Heap (max len : k)
        heap = nums[:]
        
        heapq.heapify_max(heap)

        for _ in range(k):
            ans = heapq.heappop_max(heap)
    
        return ans