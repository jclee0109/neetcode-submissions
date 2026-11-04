class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: int) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node: Optional[Node]) -> None:
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        node = self.cache[key]

        # 최근 사용으로 이동
        self.remove(node)
        self.insert(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key]=node
            self.insert(node)

            if len(self.cache.keys()) > self.capacity:
                head = self.left.next
                self.remove(head)
                self.cache.pop(head.key)

        
