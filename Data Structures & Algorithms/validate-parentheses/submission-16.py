class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}":"{", "]":"[", ")":"("}
        stack = []

        for x in s:
            if x in pairs:
                if not stack: 
                    return False

                if stack[-1] != pairs[x]:
                    return False
            
                else:
                    stack.pop()

            else:
                stack.append(x)

        return True if not stack else False

