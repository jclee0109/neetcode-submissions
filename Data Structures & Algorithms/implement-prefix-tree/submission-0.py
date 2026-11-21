class Node:
    def __init__(self, val:int=0, is_tail:bool=False):
        self.val = val
        self.next_node = {}
        self.is_tail = is_tail

class PrefixTree:
    def __init__(self):
        self.dummy = Node()

    def insert(self, word: str) -> None:
        cur = self.dummy

        for c in word:
            if c not in cur.next_node:
                cur.next_node[c] = Node(val=c)
            cur = cur.next_node[c]
        cur.is_tail = True

    def search(self, word: str) -> bool:
        cur = self.dummy
        for c in word:
            if c not in cur.next_node:
                return False
            cur = cur.next_node[c]
        
        return cur.is_tail

    def startsWith(self, prefix: str) -> bool:
        cur = self.dummy
        for c in prefix:
            if c not in cur.next_node:
                return False
            cur = cur.next_node[c]
        
        return True