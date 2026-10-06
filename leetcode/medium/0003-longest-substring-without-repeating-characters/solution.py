class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l ,maxcount = 0,0
        window = set()
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            maxcount = max(maxcount,r-l+1)    
            window.add(s[r])
        return maxcount
