# Longest Substring Without Repeating Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, find the length of the  **longest**   **substring**  without duplicate characters.

 

 **Example 1:** 

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

```

 **Example 2:** 

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

 **Example 3:** 

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

 **Constraints:** 

- 0 <= s.length <= 105
- s consists of English letters, digits, symbols and spaces.

## Solution

**Language:** Python  
**Runtime:** 429 ms (beats 36.60%)  
**Memory:** 16.9 MB (beats 13.52%)  
**Submitted:** 2026-10-06T19:12:28.995Z  

```py
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

```

---

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)