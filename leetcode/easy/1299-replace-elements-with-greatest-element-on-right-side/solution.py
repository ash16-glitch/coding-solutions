class Solution(object):
    def replaceElements(self, arr):
        rightmax = -1
        for i in range(len(arr) -1,-1,-1):
            currmax = max(rightmax, arr[i])
            arr[i] = rightmax
            rightmax = currmax
        return arr
        