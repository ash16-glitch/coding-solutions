# Reverse String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

 

 **Example 1:** 

```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

```

 **Example 2:** 

```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s[i] is a printable ascii character.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 53.97%)  
**Memory:** 19.8 MB (beats 77.18%)  
**Submitted:** 2026-10-13T14:25:44.732Z  

```py
class Solution(object):
    def reverseString(self, s):
        l = 0
        r = len(s)-1
        while l<r:
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
        return s
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-string/)