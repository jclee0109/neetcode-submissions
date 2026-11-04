class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd 알고리즘으로 (fast, slow)
        slow = nums[0]
        fast = nums[0] # 포인터를 배열 idx 자체로 하는거임

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # slow랑 fast랑 만남
        # slow = a + b 이동 (미팅 지점 a+b)
        # fast = a + b + k*c = 2(a+b)
        # thus, k*c = a+b
        # k*c - b (fast->entry point) = a
        # a (slow->entry point) = a
        slow = nums[0]
        while slow != fast:
            slow=nums[slow]
            fast=nums[fast]

        return slow