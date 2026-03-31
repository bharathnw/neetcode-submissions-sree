class Solution:
    def __init__(self):
        self.secretKey = '@$%^sree@$%^'
        self.seperator = '|EF@EF|'

    def encode(self, strs: List[str]) -> str:
        res = ""
        for index, word in enumerate(strs):
            res += str(len(word)) + self.seperator + word + self.secretKey
        return res

    def decode(self, s: str) -> List[str]:
        
        res = []
        for word in s.split(self.secretKey):
            print(word)
            actWord = word.split(self.seperator)
            if len(actWord) == 2:
                res.append(actWord[1])
        return res


