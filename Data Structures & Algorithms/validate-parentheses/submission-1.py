class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {')': '(', ']': '[', '}': '{'}

        stack = []

        for c in s:
            if c in pairs:
                #its a closing bracket
                #check if it matches the top of the stack
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else: #its an opening bracket
                stack.append(c)
            
        return not stack #stack isn't empty






