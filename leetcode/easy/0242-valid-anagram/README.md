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
**Runtime:** 23 ms (beats 46.71%)  
**Memory:** 13.4 MB (beats 40.11%)  
**Submitted:** 2026-10-11T10:02:06.643Z  

```py
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
```

---

[View on LeetCode](https://leetcode.com/problems/valid-anagram/)