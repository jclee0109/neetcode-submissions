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
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "*":
                    result = num1*num2
                else: # operator == "/"
                    result = int(num1/num2)
                stack.append(result)
            
            else:
                stack.append(int(token))
        return stack[0] if len(stack) == 1 else False
