class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        t_prod = 1
        zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
                
            else:
                t_prod = t_prod * num
            
        result = []
        for num in nums:
            if num == 0:
                if zero_cnt == 1: #exactly one zero
                    result.append(int(t_prod))
                else:
                    result.append(0)
            else:
                if zero_cnt >= 1:
                    result.append(0)
                else:
                    result.append(int(t_prod/num))

        return result