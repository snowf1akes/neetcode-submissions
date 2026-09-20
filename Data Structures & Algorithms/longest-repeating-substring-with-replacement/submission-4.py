class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        max_len = 0
        counts = defaultdict(int)

        for R in range(len(s)):
            counts[s[R]] += 1

            while (R - L + 1) - max(counts.values()) > k:
                counts[s[L]] -= 1
                L += 1
                
            max_len = max(max_len, R - L + 1)

        return max_len

        
        