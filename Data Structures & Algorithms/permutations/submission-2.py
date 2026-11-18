class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i:int) -> None: # i 를 depth, dfs(i): i-1까진 fix 됐음, i~끝까지 순서 바꿈
            if i == len(nums):
                ans.append(nums[:])
                return 

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        
        dfs(0)
        return ans
            
