class Solution(object):
    def maxSubArray(self, nums):
        currmax = 0
        maxsum = nums[0]
        for i in range(len(nums)):
            currmax +=nums[i]
            if currmax>maxsum:
                maxsum = currmax
            if currmax<0:
                currmax = 0
        return maxsum