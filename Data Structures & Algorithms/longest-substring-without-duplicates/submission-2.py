class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = set()

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
            else:
                max_len = max(len(seen), max_len)
                for j in range(i-len(seen), i):
                    if s[j] == s[i]:
                        break
                    else:
                        seen.remove(s[j])
                
        return max(max_len, len(seen))

