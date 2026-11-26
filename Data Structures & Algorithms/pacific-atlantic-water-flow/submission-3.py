from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]

        p_queue = deque()
        a_queue = deque()

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(queue, visited):
            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if not (0 <= nr < n and 0 <= nc < m):
                        continue

                    if visited[nr][nc]:
                        continue

                    if heights[nr][nc] < heights[row][col]:
                        continue

                    visited[nr][nc] = True
                    queue.append((nr, nc))

        for row in range(n):
            for col in range(m):
                if row == 0 or col == 0:
                    pacific[row][col] = True
                    p_queue.append((row, col))

                if row == n - 1 or col == m - 1:
                    atlantic[row][col] = True
                    a_queue.append((row, col))

        bfs(p_queue, pacific)
        bfs(a_queue, atlantic)

        result = []

        for row in range(n):
            for col in range(m):
                if pacific[row][col] and atlantic[row][col]:
                    result.append([row, col])

        return result