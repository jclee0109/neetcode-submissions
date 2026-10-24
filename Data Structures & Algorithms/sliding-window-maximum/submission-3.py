from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i in range(len(nums)):
            # dq에서 나보다 작은 값들 제거
            target = nums[i]    
            
            while len(dq) > 0:
                idx = dq.pop()
                candidate = nums[idx]
            
                if candidate < target:
                    continue
                else:
                    dq.append(idx)
                    break
            dq.append(i)

            # 2. 왼쪽에서 인덱스 제거
            while len(dq) > 0:
                idx = dq.popleft()
                if idx <= i - k:
                    continue
                else:
                    dq.appendleft(idx)
                    break

            if i < k-1:
                continue

            else:
                idx = dq.popleft()
                max_num = nums[idx]
                dq.appendleft(idx)
                ans.append(max_num)
        return ans
        