class Solution:
    def isValid(self, s: str) -> bool:
        #dictionary with reverse ones inside as key? 
        res = []
        seen = {')':'(', '}': '{', ']':'['} 

        for i in range(len(s)):
            char = s[i]
            if char in seen:
                if res and res[-1] == seen[char]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)

        if len(res) == 0:
            return True
        else:
            return False
