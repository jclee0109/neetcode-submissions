from collections import deque

class TrieNode:
    def __init__(self, is_end=False):
        self.is_end = is_end
        self.child = {}

class WordDictionary:
    def __init__(self):
        self.start = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.start

        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        candidates = deque([self.start])

        for c in word:
            n = len(candidates)
            # .이면 현재 child를 다 돌아봐야됨.
            if c == '.':
                for _ in range(n):
                    candid = candidates.popleft()
                    for key, next_node in candid.child.items():
                        candidates.append(next_node)
                continue
            
            for _ in range(n):
                candid = candidates.popleft()
                if c in candid.child:
                    node = candid.child[c]
                    candidates = deque([node])
                    break
            else:
                return False
        
        if c == '.':
            for candid in candidates:
                if candid.is_end:
                    return True    
            return False

        print(word, candidates[0].is_end)
        return candidates[0].is_end
        
