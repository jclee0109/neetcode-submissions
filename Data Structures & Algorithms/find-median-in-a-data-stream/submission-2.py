class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []        

    def addNum(self, num: int) -> None:
        if len(self.left_heap) == len(self.right_heap):
            if len(self.left_heap) == 0 or num <= self.right_heap[0]:
                heapq.heappush_max(self.left_heap, num)
            else:
                right_min = heapq.heappop(self.right_heap)
                heapq.heappush_max(self.left_heap, right_min)
                heapq.heappush(self.right_heap, num)
        else:
            if num >= self.left_heap[0]:
                heapq.heappush(self.right_heap, num)
            else:
                left_max = heapq.heappop_max(self.left_heap)
                heapq.heappush(self.right_heap, left_max)
                heapq.heappush_max(self.left_heap, num)
        
        return None

    def findMedian(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (self.left_heap[0] + self.right_heap[0])/2
        else:
            print(self.left_heap, self.right_heap)
            return self.left_heap[0]
        
        