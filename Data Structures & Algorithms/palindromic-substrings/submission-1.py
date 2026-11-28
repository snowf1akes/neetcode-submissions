class Solution:
    def countSubstrings(self, s: str) -> int:
        resnum = 0

        for i in range(len(s)):
            resnum += self.countPalindromes(s, i , i)
            resnum += self.countPalindromes(s, i, i + 1)
        return resnum

    def countPalindromes(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res


