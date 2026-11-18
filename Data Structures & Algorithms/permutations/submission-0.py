class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        nums_set = set(nums)
        cur_set = set()

        def dfs(i:int) -> None: # i를 깊이라고 해도 될듯
            if i == len(nums):
                ans.append(cur[:])
                return
            
            for num in nums_set-cur_set:
                cur.append(num)
                cur_set.add(num)
                dfs(i+1)
                cur.pop()
                cur_set.remove(num)
        
        dfs(0)
        return ans