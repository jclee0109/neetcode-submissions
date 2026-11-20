class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        cur = []

        def dfs(i:int)->None:
            if len(digits) == 0:
                return
            # i는 idx (34) 일때, 3이면 1, 4이면 2
            if i == len(digits):
                ans.append("".join(cur))
                return
            
            char_candid = num_to_char[digits[i]]
            for c in char_candid:
                cur.append(c)
                dfs(i+1)
                cur.pop()
        
        dfs(0)
        return ans