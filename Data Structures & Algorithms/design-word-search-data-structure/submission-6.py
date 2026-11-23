class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i:int, node:Optional[TrieNode]) -> bool:
            if i == len(word):
                return node.is_end
            
            c = word[i]
            
            if c == ".":
                for child in node.child.values():
                    if dfs(i+1, child):
                        return True
                return False
            
            if c not in node.child:
                return False

            return dfs(i+1, node.child[c])
        
        return dfs(0, self.root)



        
