class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer를 활용해서 풀어보자.
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area


            
        