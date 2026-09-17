class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total = 0, 0
        length = float('inf')

        #loop add right pointer to total, then drop left pointer if exceeds target, until its minimum 
        for R in range(len(nums)):
            total += nums[R]

            #check if it exceeds target?
            while total >= target:
                length = min(R - L + 1, length) #find minimum length thats still >= target
                total -= nums[L] #drop left pointer
                L += 1 #move left pointer up one
        return 0 if length == float('inf') else length
