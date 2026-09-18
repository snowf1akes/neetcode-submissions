class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R = 0, 0
        window = set()
        length = 0

        for R in range(len(s)):
            while s[R] in window: # if duplicate, remove left then L += 1
                window.remove(s[L])
                L += 1
            window.add(s[R]) # add regardless of condition
            length = max(length, len(window))
        return length

        