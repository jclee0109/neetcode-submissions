class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        cur = []

        def dfs(i:int)->None:
            if i >= len(nums):
                ans.append(cur[:])
                return
            
            cur.append(nums[i])
            dfs(i+1)

            start = i+1
            while start < len(nums) and nums[i] == nums[start]:
                start += 1
            
            cur.pop()
            dfs(start)
        
        dfs(0)
        return ans