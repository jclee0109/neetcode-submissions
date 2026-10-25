class MinStack:

    def __init__(self):
        self.idx = 0
        self.stack = [float("inf")]*(3*10**4)
        self.minimum = [float("inf")]*(3*10**4)
        return None

    def push(self, val: int) -> None:
        idx = self.idx + 1
        self.stack[idx] = val
        self.minimum[idx] = min(val, self.minimum[idx-1])
        self.idx += 1
        return None

    def pop(self) -> None:
        result = self.stack[self.idx]
        self.stack[self.idx] = float("inf")
        self.idx -= 1
        return result

    def top(self) -> int:
        return self.stack[self.idx]

    def getMin(self) -> int:
        return self.minimum[self.idx]

        
