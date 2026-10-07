class Solution(object):
    def getConcatenation(self, nums):
        arr=[]
        for i in range(2):
            for j in nums:
                arr.append(j)
        return arr