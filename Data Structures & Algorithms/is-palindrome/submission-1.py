class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer l, from beginning, r from back. so like a reverse search? 
        l = 0
        r = len(s) - 1
        #condition for true
        #while l == r, l+= 1, r -=1, if index of l and r are equal and value are the same --> return True
        #condition for false
        #outisde of while loop
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

        