import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]', '', s).lower()
        print(s)
        for i in range(len(s)//2):
            if s[i] == s[len(s)-1-i]:
                continue
            else:
                return False
        
        return True