class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_cnt = dict({s[0]:1})
        char_max_set = set(s[0])
        char_max = 1
        max_len = 0

        if len(s) == 1:
            return 1

        left = 0
        right = 1

        while left < right:
            while right < len(s):
                target = s[right]
                char_cnt[target] = char_cnt.get(target, 0) + 1
                if target in char_max_set:
                    char_max_set = set(target)
                    char_max = char_cnt[target]
                elif char_cnt[target] == char_max: 
                    char_max_set.add(target)

                max_len = max(max_len, min(char_max+k, right-left+1))
                if char_max + k < right-left + 1:
                    right += 1
                    break

                right += 1
            
            target = s[left]
            if target in char_max_set:
                char_max_set.remove(target)
            char_cnt[target] -= 1
            left += 1
        
        return max_len
        

        

        
