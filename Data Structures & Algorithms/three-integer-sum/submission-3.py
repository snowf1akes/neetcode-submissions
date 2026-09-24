class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #if theres no result that return []
        #edge case 0 sum up return bracket of 0? 
        res = []
        #sort input arry
        nums.sort()
        #check for -nums[i] = nums[j] + nums[k]
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]: #dupe checker
                continue

            #two pointer here
            l = i + 1
            r = len(nums) -1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:#too big reduce sum, move r left
                    r -= 1
                elif threeSum < 0: #too small increase sum
                    l += 1 
                elif threeSum == 0: #update res
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res