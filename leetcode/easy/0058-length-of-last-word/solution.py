class Solution(object):
    def lengthOfLastWord(self, s):
        last = len(s)-1
        length = 0
        for i in range (last ,-1,-1):
            if s[i]!= " ":
                length+=1
            elif length > 0:
                break
        return length
