class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quick Select
        target = len(nums) - k

        def quick_select(left, right):
            p = left
            pivot = nums[right]
            
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[p], nums[right] = nums[right], nums[p]

            if p == target:
                return nums[p]
            
            elif p < target:
                return quick_select(p+1, right)
            
            else:
                return quick_select(left, p-1)

        return quick_select(0, len(nums)-1)


            