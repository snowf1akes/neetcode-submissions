class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n

        for i in range(n):
            maxRight = -1
            for j in range(i + 1, n):
                if arr[j] > maxRight:
                    maxRight = arr[j]
            ans[i] = maxRight
            
        return ans
