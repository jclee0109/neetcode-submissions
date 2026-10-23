class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        min_len = float('inf')
        need = dict()
        window = dict()

        for c in t:
            need[c] = need.get(c, 0) + 1
        
        left = 0
        right = 0
        ans = ""

        if len(t) > len(s):
            return ans

        while left < len(s):
            # left 선택 조건 (target에 없거나 이미 윈도우에 여유가 있을때 지나치기)
            if s[left] not in need.keys() or window.get(s[left], 0) >= need[s[left]]:
                left += 1
                continue
            else: # left 선택 됐음 -> max len 뽑아보고, 같은거 만나면 left 점프
                right = left

                while right < len(s):
                    if s[right] in need.keys():
                        window[s[right]] = window.get(s[right], 0) + 1
                    for k_need in need.keys():
                        if window.get(k_need, 0) < need[k_need]:
                            break 
                    else: # 포함된 문자열을 찾음
                        # left 올리고 break (최소 유지)
                        while left <= right:
                            if s[left] not in need.keys():
                                left += 1
                                continue

                            if window[s[left]] > need[s[left]]:
                                window[s[left]] -= 1
                                left += 1
                            else:
                                if min_len > right-left:
                                    ans = s[left:right+1]
                                    min_len = right-left
                                break
                    right += 1

                return ans
        return ans
