class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

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
                if (
                    board[i][j] == 'O' and
                    ((i==0 or i==n-1) or
                    (j==0 or j==m-1))
                    
                ):
                    queue.append((i,j))
                    board[i][j] = "T"
        
        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    0 > nr or n <= nr or
                    0 > nc or m <= nc or
                    board[nr][nc] == 'X' or
                    board[nr][nc] == 'T'
                ):
                    continue

                queue.append((nr,nc))
                board[nr][nc] = "T"
    
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"