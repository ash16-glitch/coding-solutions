class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxsum =0
        currsum = 0
        for i in nums:
            if i >0:
                currsum+=i
            if currsum>maxsum:
                maxsum = currsum
            if i ==0:
                currsum = 0
        return maxsum

        """
        :type nums: List[int]
        :rtype: int
        """
        