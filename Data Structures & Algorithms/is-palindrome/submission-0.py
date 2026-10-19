import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s = re.sub('[^A-Za-z0-9]', '', s)
        print(s)
        for i in range(len(s)//2):
            if s[i] == s[len(s)-1-i]:
                continue
            else:
                return False
        
        return True