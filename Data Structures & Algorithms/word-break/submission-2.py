class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        #dp[i] means s[0:i] can be seg
        dp = [False] * (n + 1)
        dp[0] = True #base case empty string

        for i in range(1, n + 1):
            for j in range(i):
                #if prefix up to j is doable
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break #once we found valid split move to next if
            
        return dp[n]
