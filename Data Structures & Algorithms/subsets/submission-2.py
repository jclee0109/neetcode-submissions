class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        subset = self.subsets(nums[1:])
        ans = []

        for each_set in subset:
            ans.append(each_set)
            ans.append([nums[0]]+each_set)

        return ans