class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        cur = [] # [(0,1),(1,3),(2,1),(3,2) 이렇게 가자.
        
        def is_available_nq(cur:List[tuple], candidate:tuple)->bool:
            for row, col in cur:
                # 같은 행이나 열
                if candidate[0] == row or candidate[1] == col:
                    return False
                # diagonal
                if abs(candidate[1]-col)/(candidate[0]-row) == 1:
                    return False
            return True

        def _get_output_form(cur:List[tuple])->List[str]:
            result = []
            
            for row, col in cur:
                result.append("."*(col) + "Q" + "."*(n-col-1))
            
            return result

        def dfs(row:int) -> None:
            if row == n:
                ans.append(_get_output_form(cur))
                return
            
            for col in range(n):
                candidate = (row, col)
                if is_available_nq(cur, candidate):
                    cur.append(candidate)
                    dfs(row+1)
                    cur.pop()

        dfs(0)
        return ans        