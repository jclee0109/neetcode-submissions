import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 결국 적당한 indx 찾는거니까, binary search로 찾아보자.
        left = 1
        right = max(piles)
        min_k = float('inf')

        while left <= right:
            mid = (left+right)//2
            total = 0
            for pile in piles:
                time = pile//mid if pile%mid==0 else pile//mid+1
                total += time
                if total > h:
                    left = mid + 1
                    break
            if total <= h:
                min_k = min(min_k, mid)
                right = mid - 1
        
        return min_k
        