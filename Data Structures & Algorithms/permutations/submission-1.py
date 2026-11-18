class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        cur_set = set()

        def dfs(i:int) -> None:
            if i == len(nums):
                ans.append(cur[:])
                return None
            
            for num in nums:
                if num in cur_set:
                    continue
                
                cur.append(num)
                cur_set.add(num)

                dfs(i+1)

                cur.pop()
                cur_set.remove(num)
            
        dfs(0)
        return ans