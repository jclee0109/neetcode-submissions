class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if len(stack) > 0:
                last = stack.pop()
                if c == "]" or c==")" or c=="}":
                    if last == "(" and c== ")":
                        continue
                    elif last == "{" and c=="}":
                        continue
                    elif last == "[" and c=="]":
                        continue
                    else:
                        return False
                else:
                    stack.append(last)
                    stack.append(c)
                    continue

            else:
                if c == "]" or c==")" or c=="}":
                    return False
                else:
                    stack.append(c)
                    continue
            
        if len(stack) > 0:
            return False
        else: return True
