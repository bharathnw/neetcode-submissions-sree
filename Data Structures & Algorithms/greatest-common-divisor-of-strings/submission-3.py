class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        

        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a
        
        denominator = str1 if len(str1) <= len(str2) else str2
        numerator = str2 if denominator == str1 else str1
        startIndex = 0
        endIndex = len(denominator)

        while endIndex <= len(numerator):
            if numerator[startIndex:endIndex] != denominator:
                return ""
            startIndex += len(denominator)
            endIndex += len(denominator)
        return numerator[-(gcd(len(numerator), len(denominator))):]
            