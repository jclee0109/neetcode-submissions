class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # bfs로 풀자.

        n = len(grid)
        m = len(grid[0])

        visited = [[False]*m for _ in range(n)]
        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]

        def bfs(i:int, j:int)->int:
            queue = deque([(i,j)])
            visited[i][j] = True
            island = [(i, j)]

            while queue:
                i, j = queue.popleft()

                for di, dj in directions:
                    ni = i+di
                    nj = j+dj

                    if (0 <= ni and ni < n and
                        0 <= nj and nj < m and
                        not visited[ni][nj] and
                        grid[ni][nj] == 1):
                        queue.append((ni, nj))
                        visited[ni][nj] = True
                        island.append((ni, nj))
            return len(island)
        
        max_size = 0
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 1:
                    max_size = max(max_size, bfs(i,j))

        return max_size