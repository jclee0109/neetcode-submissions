class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()

        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1

        for c in t:
            if c in t_dict:
                t_dict[c] += 1
            else:
                t_dict[c] = 1

        if len(s_dict) != len(t_dict):
            return False
        else:
            for k, i in s_dict.items():
                if k not in t_dict.keys():
                    return False
                elif s_dict[k] != t_dict[k]:
                    return False
            else:
                return True

