class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    last = stack.pop()
                    if pairs[last] != c:
                        return False
            
        return len(stack) == 0