class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            digit = 0
            while i>0:
                i//=10
                digit+=1
            if digit%2==0:
                count+=1
        return count