class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string = encoded_string + "간" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = s.split("간")
        return decoded_string[1:]
