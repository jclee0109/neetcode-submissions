class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [[], [nums[0]]]
        print(nums)
        subset = self.subsets(nums[1:])
        print(subset)
        ans = []

        for each_set in subset:
            ans.append(each_set)
            ans.append([nums[0]]+each_set)

        return ans