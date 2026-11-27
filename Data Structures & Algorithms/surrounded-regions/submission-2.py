class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        visited = [[False]*m for _ in range(n)]

        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]

        # bfs (not multi-source)
        queue = deque()
        o_list = []

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X':
                    continue
                if (
                    not visited[i][j] and
                    (i==0 or i==n-1) or
                    (j==0 or j==m-1)
                    
                ):
                    queue.append((i,j))
                    visited[i][j] = True
                o_list.append((i,j))
        
        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    0 > nr or n <= nr or
                    0 > nc or m <= nc or
                    visited[nr][nc] or
                    board[nr][nc] == 'X'
                ):
                    continue

                queue.append((nr,nc))
                visited[nr][nc] = True
    

        for row, col in o_list:
            if not visited[row][col]:
                board[row][col] = 'X'
        
