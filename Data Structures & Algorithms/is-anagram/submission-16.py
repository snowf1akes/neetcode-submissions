from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countT = Counter(t)

        for ch in s:
            if ch not in countT or countT[ch] == 0:
                return False
            countT[ch] -= 1

        return True