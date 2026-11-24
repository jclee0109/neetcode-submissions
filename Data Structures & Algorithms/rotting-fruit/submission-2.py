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
        cnt = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    cnt += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
                    grid[row][col] = 0
                    cnt += 1
        
        max_time = 0
        while queue:
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
                time_spent = -grid[row][col]+1
                grid[nr][nc] = -time_spent
                max_time = max(max_time, time_spent)
                cnt += 1
        
        if cnt < n*m:
            return -1
        
        return max_time
