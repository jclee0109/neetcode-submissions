class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(board) # 행 개수
        M = len(board[0]) # 열 개수

        visited = [[False]*M for _ in range(N)]
        cur = []
        
        def dfs(i, j):
            # 지금 노드 방문 체크
            if len(cur) == len(word):
                candidate = "".join(cur)
                if candidate == word:
                    return True
                return False
            
            if len(cur) > len(word):
                return False
            
            # 우로 이동
            if j+1 < M and not visited[i][j+1]:
                cur.append(board[i][j+1])
                visited[i][j+1] = True
                if dfs(i, j+1):
                    return True
                visited[i][j+1] = False
                cur.pop()
            
            # 하로 이동
            if i+1 < N and not visited[i+1][j]:
                cur.append(board[i+1][j])
                visited[i+1][j] = True
                if dfs(i+1, j):
                    return True
                visited[i+1][j] = False
                cur.pop()

            # 상으로 이동
            if i-1 >= 0 and not visited[i-1][j]:
                cur.append(board[i-1][j])
                visited[i-1][j] = True
                if dfs(i-1, j):
                    return True
                visited[i-1][j] = False
                cur.pop()

            # 좌로 이동
            if j-1 >= 0 and not visited[i][j-1]:
                cur.append(board[i][j-1])
                visited[i][j-1] = True
                if dfs(i, j-1):
                    return True
                visited[i][j-1] = False
                cur.pop()

        for i in range(N):
            for j in range(M):
                cur = [board[i][j]]
                visited[i][j] = True
                ans = dfs(i,j)
                visited[i][j] = False
                cur.pop()
                if ans:
                    return True
                
        return False

        