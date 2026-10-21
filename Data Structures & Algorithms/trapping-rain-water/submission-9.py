class Solution:
    def trap(self, height: List[int]) -> int:
        # 길이 예외처리 1, 2일때 처리
        n = len(height)

        if n == 1 or n == 2:
            return 0 # 길이 1,2 에서는 무엇이든 담길 수 없음
        
        ans = 0
        left = 0
        right = 0
        future = 0
        # find local maximum (n>=3)
        while left <= len(height)-1:
            while left < len(height):
                if self.is_local_max(left, height):
                    break
                left += 1
            else:
                return ans

            right = left+1
            right_exist_flag = False

            # left를 찾았으면 next right 찾기
            while right < len(height):
                if self.is_local_max(right, height):
                    right_exist_flag = True
                    future = right+1
                    future_flag = False
                    if height[left] > height[right]:
                        while future < len(height):
                            if self.is_local_max(future, height) and height[right] <= height[future]:
                                right = future
                                future_flag = True
                                break
                            else:
                                future += 1
                        if future_flag:
                            continue
                    break
                else:
                    right+=1

            if not right_exist_flag:
                return ans
            
            # h_l > h_r이면, 이후에 더 큰 right 등장시 물이 더 채워질 수 있음
            # future에 조건 만족하는거 있나 찾고, 있으면 그걸 right으로, 없으면 끝
            between = list(map(lambda h: max(0, min(height[right], height[left]) - h), height[left+1:right]))
            area = sum(between)
            ans += area
            left = right
            
        # 각 local max 양 점 순회 (left, right) ->
        return ans

    def is_local_max(self, i: int, height: List[int])->bool:
        # 양 끝 예외 처리 (시작, n>=3)
        if i == 0:
            if height[i] > height[i+1]:
                return True
            else:
                return False
        # 양 끝 예외 처리 (끝, n>=3)
        elif i == len(height)-1:
            if height[i-1] < height[i]:
                return True
            else:
                return False
        # 가운데 (n>=3)
        else:
            if height[i-1] <= height[i] and height[i] >= height[i+1]:
                return True
            else:
                False
        