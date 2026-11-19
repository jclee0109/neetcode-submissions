class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        cur = []
        open_cnt = 0
        close_cnt = 0

        def dfs(i:int)->None:
            nonlocal open_cnt, close_cnt

            if i==2*n:
                if cur[-1] == ")":
                    ans.append("".join(cur))
                return
            
            if open_cnt > n or open_cnt < close_cnt:
                return
            
            cur.append("(")
            open_cnt += 1
            dfs(i+1)
            open_cnt -= 1
            cur.pop()

            cur.append(")")
            close_cnt += 1
            dfs(i+1)
            close_cnt -= 1
            cur.pop()

        dfs(0)
        return ans