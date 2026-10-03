class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        counter = 0 # global counter to count threshold
        l = 0 # left pointer window
        maxsum = 0 # max sum of windows
        for r in range(len(arr)):
            maxsum = maxsum+arr[r]
            if r-l+1 >k:
                maxsum = maxsum - arr[l]
                l+=1 
            
            if r-l+1 == k:
                if maxsum/k >= threshold:
                    counter+=1
        return counter 