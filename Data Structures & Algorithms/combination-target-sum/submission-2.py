class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target: # base case if we succed
                res.append(cur.copy())
                return 
            #i is out of bounds or total is over target
            if i >= len(nums) or total > target:
                return 

            #recursive step, include extra i from cur
            cur.append(nums[i])
            dfs(i, cur, total + nums[i]) 
            cur.pop()

            dfs(i + 1, cur, total) 
        dfs(0, [], 0)
        return res