# Trie로 풀기
# 일단 prefix 겹치는 단어들이 있으면 이걸 최대한 pruning 해보자
class TrieNode:
    def __init__(self):
        self.child = {}
        self.idx = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, idx):
        node = self.root

        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        
        node.idx = idx


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])

        trie = Trie()

        for idx, word in enumerate(words):
            trie.insert(word, idx)
        
        node = trie.root
        result = []
        visited = [[False]*m for _ in range(n)]
        moves = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]


        def dfs(row, col, node) -> None:
            if board[row][col] not in node.child:
                return
            node = node.child[board[row][col]]
            if node.idx != -1:
                result.append(words[node.idx])
                node.idx = -1

            if len(node.child) == 0:
                return

            for dx, dy in moves:
                x = row + dx
                y = col + dy

                if (0 > x or x >= n or 
                    0 > y or y >= m or
                    visited[x][y]
                ):
                    continue
                
                visited[x][y] = True
                dfs(x, y, node)
                visited[x][y] = False
            
            return


        for row in range(n):
            for col in range(m):
                visited[row][col] = True
                dfs(row, col, node)
                visited[row][col] = False
                    
        return result


        