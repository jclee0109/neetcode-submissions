class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        cur = []
        substrings = []

        def is_palindrome(s:List[str]):
            for i in range(len(s)//2):
                if s[i] != s[len(s)-1-i]:
                    return False
            
            return True

        def dfs(i:int) -> None:
            nonlocal cur
            # 반환조건 : 끝까지 탐색
            if i == len(s):
                if is_palindrome(cur) and len(cur) > 0:
                    substrings.append("".join(cur))
                    ans.append(substrings[:])
                    substrings.pop()
                return
                

            # 지금 cur가 palindrome이면 
            # 1. 지금까지 완성된 팰린드롬을 저장한다. cur 초기화
            # 2. 저장하지 않고, 다음 string을 붙인다.
            cur.append(s[i])
            if is_palindrome(cur):
                palindrome = cur[:]
                substrings.append("".join(cur))
                cur = []
                dfs(i+1)
                substrings.pop()
                cur = palindrome
                dfs(i+1)
                # palindrome = cur[:]
                # substrings.append(palindrome)
                # cur = []
                # dfs(i+1)
                # substrings.pop()
                # dfs(i+1)
                
            # palindrome이 아니면
            # 2. 저장하지 않고 다음 string을 붙인다.
            else:
                dfs(i+1)

            
        dfs(0)
        return ans