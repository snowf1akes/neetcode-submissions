class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h = {}
        res = []
        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                sum *= -1

                if sum in h:
                    if h[sum] != i and h[sum] != j:
                        result_element = [nums[i] , nums[j], sum]
                        result_element.sort()
                        if result_element not in res:
                            res.append(result_element)
        return res



                




                
                