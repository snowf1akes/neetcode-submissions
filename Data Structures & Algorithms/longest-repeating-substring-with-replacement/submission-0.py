from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #hashmap 
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            #while valid: window length - highest freq count val <= to k
            while (r - l + 1) - max(count.values()) > k: 
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1) #length of res + size of window
        return res



                    


