# Add Binary

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two binary strings `a` and `b`, return  *their sum as a binary string*.

 

Original
Python
 **Example 1:** 

```
Input: a = "11", b = "1"
Output: "100"

```

 **Example 2:** 

```
Input: a = "1010", b = "1011"
Output: "10101"

```

 

 **Constraints:** 

- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.

## Solution

**Language:** Python  
**Runtime:** 5 ms (beats 46.85%)  
**Memory:** 12.1 MB (beats 80.96%)  
**Submitted:** 2026-11-15T08:51:48.026Z  

```py
class Solution(object):
    def addBinary(self, a, b):
        i = len(a)-1
        j = len(b)-1
        carry = 0
        result = []
        while i>=0 or j >= 0 or carry:
            total = carry
            if i>= 0:
                total+= int(a[i])
                i-=1
            if j>=0:
                total+= int(b[j])
                j-=1
            result.append(str(total%2))
            carry = total//2
        return "".join(result[::-1])


```

---

[View on LeetCode](https://leetcode.com/problems/add-binary/)