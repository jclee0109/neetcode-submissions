class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        wait_list = []
        lefts = [-1]*len(heights)
        rights = [len(heights)]*len(heights)
        max_area = 0

        for i, height in enumerate(heights):
            if not wait_list:
                wait_list.append(i)
                continue

            if heights[wait_list[-1]] == height:
                lefts[i] = lefts[wait_list[-1]]
                wait_list.append(i)

            elif heights[wait_list[-1]] < height:
                lefts[i] = wait_list[-1]
                wait_list.append(i)
            else: # top의 height가 들어오려는거보다 클때
                # top 뺀 이후
                left = lefts[wait_list[-1]]
                while heights[left] >= height and left != -1:
                    left = lefts[left]
                
                lefts[i] = left
                # top 먼저 빼도 됨 (얘는 결정 됐거든)
                while wait_list and heights[wait_list[-1]] > height:
                    top = wait_list.pop()
                    top_height = heights[top]
                    rights[top] = i
                    top_width = rights[top] - lefts[top] - 1
                    area = top_height*top_width
                    max_area = max(area, max_area)
                
                wait_list.append(i)

        for idx in wait_list:
            area = (rights[idx]-lefts[idx]-1)*heights[idx]
            max_area = max(max_area, area)

        return max_area
                    




