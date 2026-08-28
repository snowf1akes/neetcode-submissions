from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        scount = Counter(s)
        tcount = Counter(t)

        if scount != tcount:
            return False
        else:
            return True