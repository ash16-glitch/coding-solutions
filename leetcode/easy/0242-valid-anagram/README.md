# Valid Anagram

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

 **Example 1:** 

 **Input:**  s = "anagram", t = "nagaram"

 **Output:**  true

 **Example 2:** 

 **Input:**  s = "rat", t = "car"

 **Output:**  false

 

 **Constraints:** 

- 1 <= s.length, t.length <= 5 * 104
- s and t consist of lowercase English letters.

 

 **Follow up:**  What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Solution

**Language:** Python  
**Runtime:** 18 ms (beats 64.32%)  
**Memory:** 12.4 MB (beats 86.88%)  
**Submitted:** 2026-10-11T10:00:57.447Z  

```py
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False 
        counts, countt = {},{}
        for ch in s:
            counts[ch] = counts.get(ch ,0) + 1
        for ch in t :
            countt[ch] = countt.get(ch, 0) + 1
        
        return counts == countt
```

---

[View on LeetCode](https://leetcode.com/problems/valid-anagram/)