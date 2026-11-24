from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bsf로 island 하나 쭉 찾기 -> not visited and '1' 순회하며서 탐색 -> 찾으면 bsf 반복
        queue = deque()
        n = len(grid)
        m = len(grid[0])

        visited = [[False]*m for _ in range(n)]
        cnt = 0
        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]

        def bfs(i:int, j:int)->List[(int, int)]:
            this_island = [(i,j)]
            queue.append((i,j))
            visited[i][j] = True

            while queue:
                row, col = queue.popleft()
                for drow, dcol in directions:
                    new_row = row + drow
                    new_col = col + dcol

                    if (0 <= new_row and new_row < n and
                        0 <= new_col and new_col < m and
                        not visited[new_row][new_col] and
                        grid[new_row][new_col] == '1'
                    ):
                        queue.append((new_row,new_col))
                        visited[new_row][new_col] = True
                        this_island.append((new_row,new_col))
            
            return this_island

        all_island = []

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == '1':
                    island = bfs(i,j)
                    all_island.append(island)
                    cnt += 1
        
        return cnt
        
        
        