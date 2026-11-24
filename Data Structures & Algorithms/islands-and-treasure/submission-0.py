class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        n = len(grid)
        m = len(grid[0])

        visited = [[False]*m for _ in range(n)]
        land_val = 2**31 - 1

        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]

        queue = deque([])

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))
                    visited[row][col] = True
        
        while queue:
            row, col, depth = queue.popleft()

            for dr, dc in directions:
                nr = row+dr
                nc = col+dc

                if (
                    0 > nr or nr >= n or
                    0 > nc or nc >= m or
                    grid[nr][nc] == -1 or
                    visited[nr][nc]
                ):
                    continue

                queue.append((nr, nc, depth+1))
                visited[nr][nc] = True
                grid[nr][nc] = depth+1

