class Solution(object):
    def sortedSquares(self, nums):
        res = []
        l = 0
        r = len(nums)-1
        while l<=r:
            leftsqr = nums[l]**2
            rightsqr = nums[r]**2
            if rightsqr>=leftsqr:
                res.append(rightsqr)
                r-=1
            else:
                res.append(leftsqr)
                l+=1
        return res[::-1]
        