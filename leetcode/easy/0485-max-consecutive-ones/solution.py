class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current = 0
        maxcounter = 0
        for num in nums:
            if num ==1:
                current +=1
                maxcounter = max(current, maxcounter)     
            else:
                current = 0
        return maxcounter

        """
        :type nums: List[int]
        :rtype: int
        """
        