class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        total = 0
        minarray = float('inf')
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                minarray = min(minarray, r-l+1)
                total-=nums[l]
                l+=1
        return 0 if minarray == float('inf') else minarray