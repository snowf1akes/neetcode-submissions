from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if same length
        if len(s) != len(t):
            return False

        #use a counter on s as key, then check t with counter? 
        count = Counter(s)
        #a: 2, c: 2, e: 1, r: 2
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1

        return True
        
        #don't have feature that checks freq and makes sure that matches