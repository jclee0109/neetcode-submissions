class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []

        def dfs(i:int, total) -> None:
            if target == total:
                ans.append(cur[:])
                return 
            elif target < total:
                return

            for j in range(i, len(nums)):
                cur.append(nums[j])
                dfs(j, total+nums[j])
                cur.pop()

        dfs(0, 0)
        return ans
        