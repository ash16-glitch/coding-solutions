class Solution(object):
    def maxSubarraySumCircular(self, nums):
        currmax = 0
        currmin = 0
        globalmax =nums[0]
        globalmin = nums[0]
        total = 0
        for i in range(len(nums)):
            total+=nums[i]

            # find max 
            currmax+=nums[i]
            if currmax > globalmax:
                globalmax = currmax
            if currmax<0:
                currmax = 0
        
        # find min
            currmin+=nums[i]
            if currmin <globalmin:
                globalmin = currmin
            if currmin>0:
                currmin=0

        if total - globalmin == 0:
            return globalmax
        
        totalsum = (total-globalmin)
        if totalsum> globalmax:
            return totalsum
        else:
            return globalmax

        