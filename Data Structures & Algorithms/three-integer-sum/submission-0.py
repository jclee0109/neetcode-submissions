class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 중복 제거용 (이미 확인한 건 skip)
        checked_set = set()
        ans = set()
        nums = sorted(nums)

        for i in range(len(nums)-2):
            # i 는 target에 대한 정보
            if nums[i] in checked_set:
                continue
            checked_set.add(nums[i])
            left = i+1
            right = len(nums)-1
            target = nums[i] * (-1)

            # find (크기가 target보다 작으면 left를 키우고)
            while left < right:
                if (nums[i], nums[left], nums[right]) in ans:
                    left += 1
                    right -= 1
                    continue

                current_sum = nums[left] + nums[right]
                if target == current_sum:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    continue

                elif target < current_sum:
                    right -= 1
                
                elif target > current_sum:
                    left += 1
        return list(map(list, ans))