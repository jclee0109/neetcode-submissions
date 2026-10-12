from collections import deque

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            len_s = len(s)
            encoded_string = encoded_string + f'{len_s}#' + s
        return encoded_string


    def decode(self, s: str) -> List[str]:
        queue = deque() # 숫자 넣어놓는 queue
        decoded_string = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                num = ''
                while len(queue) > 0:
                    c = queue.popleft()
                    num += str(c)
                num = int(num)
                decoded_word = ''
                for _ in range(num):
                    i += 1
                    decoded_word += s[i]
                decoded_string.append(decoded_word)
                i+=1
            elif s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                queue.append(s[i])
                i += 1
            else:
                return ['']


        return decoded_string
