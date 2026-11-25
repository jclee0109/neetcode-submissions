class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        pacific = [[False]*m for _ in range(n)]
        atlantic = [[False]*m for _ in range(n)]

        p_queue = deque([])
        a_queue = deque([])

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    pacific[i][j] = True
                    p_queue.append((i,j))
                if i == n-1 or j == m-1:
                    atlantic[i][j] = True
                    a_queue.append((i,j))
        
        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]

        result = []

        while p_queue:
            row, col = p_queue.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    0 > nr or nr >= n or
                    0 > nc or nc >= m or
                    pacific[nr][nc]
                ):
                    continue
                
                if heights[row][col] <= heights[nr][nc]:
                    pacific[nr][nc] = True
                    p_queue.append((nr, nc))
        
        while a_queue:
            row, col = a_queue.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if(
                    0 > nr or nr >= n or
                    0 > nc or nc >= m or
                    atlantic[nr][nc]
                ):
                    continue

                if heights[row][col] <= heights[nr][nc]:
                    atlantic[nr][nc] = True
                    a_queue.append((nr, nc))

        for row in range(n):
            for col in range(m):
                if pacific[row][col] and atlantic[row][col]:
                    result.append([row, col])

        return result