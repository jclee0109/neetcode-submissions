class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        ans = []
        cur = []
        num_end = {}
        for i, num in enumerate(sorted_nums):
            num_end[num] = i
        def dfs(i:int) -> None:
            if i >= len(sorted_nums):
                ans.append(cur[:])
                return 
            
            cur.append(sorted_nums[i])
            dfs(i+1)

            cur.pop()
            if i<len(sorted_nums)-1 and sorted_nums[i] == sorted_nums[i+1]:
                dfs(num_end[sorted_nums[i]]+1)
            else:
                dfs(i+1)
        
        dfs(0)
        return ans