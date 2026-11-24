class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]

        queue = deque([])
        fresh_cnt = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    fresh_cnt += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
                    grid[row][col] = 0
        
        minutes = 0
        while queue and fresh_cnt > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (
                        0 > nr or nr >= n or
                        0 > nc or nc >= m or
                        grid[nr][nc] != 1 
                    ):
                        continue
                    
                    queue.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh_cnt -= 1
            minutes += 1
        
        return minutes if fresh_cnt == 0 else -1
