class Solution:

    def __init__(self):
        self.secret = '!@#$%^&*91299@@#$%'

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "__EMPTY_LIST__"
        res = ''

        for i, s in enumerate(strs):
            res += s
            if i == len(strs) - 1:
                continue
            res += self.secret
        return res

    def decode(self, s: str) -> List[str]:
        if s == "__EMPTY_LIST__":
            return []
        if not s:
            return [""]
        return s.split(self.secret)