class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        idx_stack = []

        for i in range(len(temperatures)):
            if len(idx_stack) <= 0:
                idx_stack.append(i)
                continue
            
            while len(idx_stack) > 0:
                if temperatures[idx_stack[-1]] < temperatures[i]:
                    last_idx = idx_stack.pop()
                    ans[last_idx] = i-last_idx
                else:
                    break
                
            idx_stack.append(i)
        
        return ans
        