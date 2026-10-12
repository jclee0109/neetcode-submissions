class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n #Prod(n1, n_i)
        suffix = [1] * n #Prod(n_i+1, n_k)

        for i in range(n-1):
            prefix[i+1] = prefix[i]*nums[i]
        
        for i in range(n-1, 0, -1):
            suffix[i-1] = suffix[i]*nums[i]
        
        result = []
        for i in range(n):
            result.append(prefix[i]*suffix[i])
        
        return result
