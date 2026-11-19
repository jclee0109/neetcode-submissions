class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(board)
        M = len(board[0])

        visited = [[False]*M for _ in range(N)]

        def dfs(i, j, k): #i: row, j:col, k: word_idx
            if board[i][j] != word[k]:
                return False
            
            if k == len(word) - 1:
                return True
            
            visited[i][j] = True

            directions = [
                (0,1),
                (1,0),
                (0,-1),
                (-1,0)
            ]

            for direction in directions:
                di, dj = direction
                row = i + di
                col = j + dj

                if (0 <= row < N 
                    and 0 <= col < M 
                    and not visited[row][col]
                ):
                    if dfs(row,col,k+1):
                        return True

            visited[i][j] = False
            return False
        
        for i in range(N):
            for j in range(M):
                if dfs(i,j,0):
                    return True
        
        return False
        

