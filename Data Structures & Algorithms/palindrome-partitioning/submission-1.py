class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # i라는 그냥 index 변수 말고, start라는 변수로 정의
        # start 이전엔 이미 팰린드롬이 완성됐다고 가정.
        ans = []
        cur = []

        def is_palindrome(start:int, end:int)->bool:
            left = start
            right = end

            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True
        
        def dfs(start:int)->None:
            if start == len(s):
                ans.append(cur[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    cur.append(s[start:end+1])
                    dfs(end+1)
                    cur.pop()

        dfs(0)
        return ans
                

