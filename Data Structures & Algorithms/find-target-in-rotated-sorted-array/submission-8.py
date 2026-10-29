class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        ans = -1
        
        # left == right (마지막 하나 일때 빼고, 마지막 하나라면 while 아래로)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans = mid
                break  
            # 꺾이는 지점은 무조건 하나 or 0개
            if nums[mid] < nums[right]: # 오른쪽은 쭉 오름차순 -> 왼쪽에 꺾이는 지점
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                    continue
                else: # Mid 오른쪽에는 없으니, 왼쪽 탐색 (mid도 제거해도 됨)
                    right = mid - 1
                    continue
            else: # 왼쪽이 오름차순
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                    continue
                else:
                    left = mid + 1
                    continue
        
        return ans



                