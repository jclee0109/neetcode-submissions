class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        candidates = sorted(candidates)

        def dfs(start:int, total:int) -> None:
            if total == target:
                ans.append(cur[:])
                return

            if start == len(candidates) or total > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                cur.append(candidates[i])
                dfs(i+1, total+candidates[i])
                cur.pop()
        
        dfs(0,0)
        return ans