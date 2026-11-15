import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        print(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        print(self.heap)

        return self.heap[0]

        
