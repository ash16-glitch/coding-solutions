class Solution(object):
    def findNumbers(self, nums):
        counter = 0
        for i in nums:
            digit_count = 0
            while i>0:
                i//=10
                digit_count+=1
            if digit_count%2==0:
                counter+=1
        return counter