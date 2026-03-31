class Solution:
    def isValid(self, s: str) -> bool:
        
        valid_dict = { "}":"{",
                       ")":"(", 
                        "]":"[" }
        
        stack = []

        for para in s:
            if para in valid_dict.keys():
                if not stack or stack[-1] != valid_dict[para]:
                    return False

            elif para not in valid_dict:
                stack.append(para)
                continue
            
            stack.pop()
        return not stack



        