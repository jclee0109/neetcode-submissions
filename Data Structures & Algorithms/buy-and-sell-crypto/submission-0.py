class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        arr = [0]*n
        right_max = -1
        
        for right in range(n-1, -1, -1):
            if right_max < prices[right]:
                arr[right] = prices[right]
                right_max = prices[right]

            else:
                arr[right] = right_max
        
        return max(map(lambda i: arr[i] - prices[i], range(n)))