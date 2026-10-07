class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        window = set()
        maxcounter = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            maxcounter = max(maxcounter,r-l+1)
            window.add(s[r])
        return maxcounter
