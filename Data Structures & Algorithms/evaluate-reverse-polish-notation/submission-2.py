class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                if len(stack) <= 1:
                    return False
                
                num2 = stack.pop()
                num1 = stack.pop()
                operator = token
                
                if operator == "+":
                    result = float(num1) + float(num2)
                elif operator == "-":
                    result = float(num1) - float(num2)
                elif operator == "*":
                    result = float(num1)*float(num2)
                else: # operator == "/"
                    result = int(float(num1)/float(num2))
                stack.append(str(result))
            
            else:
                stack.append(token)
        return int(float(stack[0])) if len(stack) == 1 else False
