class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        counter = 0
        maxcounter = 0
        for num in nums:
            if num == 1:
                counter+=1
            else:
                maxcounter = max(maxcounter,counter)
                counter = 0
        return max(maxcounter,counter)


        """
        :type nums: List[int]
        :rtype: int
        """
        