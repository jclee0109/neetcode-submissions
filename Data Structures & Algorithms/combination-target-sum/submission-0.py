class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []

        def dfs(i:int) -> None:
            if target == sum(cur):
                ans.append(cur[:])
                return 
            elif target < sum(cur):
                return

            for j in range(i, len(nums)):
                cur.append(nums[j])
                dfs(j)
                cur.pop()

        dfs(0)
        return ans
        