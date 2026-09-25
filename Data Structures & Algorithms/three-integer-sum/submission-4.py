class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sorted arry
        #if -nums[i] = nums[j] + nums[k]: return i, j , k
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                #too small -> sorted, means l += 1
                if nums[i] + nums[l] + nums[r] < 0: 
                    l += 1
                #too large -> sorted, means r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1 
                else:  
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res