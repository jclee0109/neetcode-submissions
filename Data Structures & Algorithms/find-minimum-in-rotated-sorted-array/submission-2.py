class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # 꺾이는 지점은 mid와 right 사이에 있다.
                # left를 mid 지점으로
                left = mid + 1
            else:
                # 오른쪽에는 최소가 없다. mid가 최소일수도 있으니 right = mid
                right = mid

        return nums[left]