class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], [] #end output + inside small 
        n = len(nums)

        def backtrack(i, cur_sum):
            #case 1 current sum = target num
            if cur_sum == target:
                res.append(sol[:])
                return

            #case 2 cur sum is out of bounds of target or if i == n --> end of array
            if cur_sum > target or i == n:
                return
            
            #actual back track --> no more 2s, go i + 1

            backtrack(i + 1, cur_sum)

            sol.append(nums[i])
            backtrack(i, cur_sum+nums[i])
            sol.pop()

        backtrack(0, 0)
        return res

