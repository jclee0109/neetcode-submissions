class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i, num in enumerate(nums):
        #     for j in range(i, len(nums)):
        #         if i == j:
        #             continue
        #         elif nums[i] + nums[j] == target:
        #             return [i, j]
        #         else:
        #             continue
        # else:
        #     return None
        # O(n^2) -> dict로 two sum 풀이

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i
        
