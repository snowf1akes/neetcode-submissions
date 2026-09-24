from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #intial check for same length
            return False
        #hashmap --> freq, val: 
        count = Counter(s)

        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1

        return True

            




            
                

