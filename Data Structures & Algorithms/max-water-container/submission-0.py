class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current = 0
        current_left = 0

        for left in range(len(heights) - 1):
            if heights[current_left] > heights[left]:
                continue
            for right in range(left+1, len(heights)):
                width = (right-left)*min(heights[left], heights[right])
                if width > current:
                    current = width
                    current_left = left
            
        return current
