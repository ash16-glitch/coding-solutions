# Reverse Words in a String III

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Original
Python
 **Example 1:** 

```
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

```

 **Example 2:** 

```
Input: s = "Mr Ding"
Output: "rM gniD"

```

 

 **Constraints:** 

- 1 <= s.length <= 5 * 104
- s contains printable ASCII characters.
- s does not contain any leading or trailing spaces.
- There is at least one word in s.
- All the words in s are separated by a single space.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 59.10%)  
**Memory:** 12.7 MB (beats 88.21%)  
**Submitted:** 2026-11-15T12:36:39.095Z  

```py
class Solution(object):
    def reverseWords(self, s):
        words = s.split(" ")
        result = []
        for word in words:
            result.append(word[::-1])
        return " ".join(result)
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-words-in-a-string-iii/)