class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        counts , countt = {}, {}
        for ch in s:
            counts[ch] = counts.get(ch,0)+1
        for ch in t:
            countt[ch]= countt.get(ch,0)+1
        
        return counts == countt