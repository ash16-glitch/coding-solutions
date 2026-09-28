class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxcount = 0
        currentcounter = 0
        for num in nums:
            if num ==1:
                currentcounter +=1
                maxcount = max(maxcount,currentcounter)
            else:
                currentcounter = 0
        return maxcount

        """
        :type nums: List[int]
        :rtype: int
        """
        