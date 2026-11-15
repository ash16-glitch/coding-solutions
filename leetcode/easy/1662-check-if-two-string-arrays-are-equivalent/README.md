# Check If Two String Arrays are Equivalent

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two string arrays `word1` and `word2`, return `true` *if the two arrays  **represent**  the same string, and* `false` *otherwise.* 

A string is  **represented**  by an array if the array elements concatenated  **in order**  forms the string.

 

Original
Python
 **Example 1:** 

```
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
```

 **Example 2:** 

```
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

```

 **Example 3:** 

```
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

```

 

 **Constraints:** 

- 1 <= word1.length, word2.length <= 103
- 1 <= word1[i].length, word2[i].length <= 103
- 1 <= sum(word1[i].length), sum(word2[i].length) <= 103
- word1[i] and word2[i] consist of lowercase letters.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 7.08%)  
**Memory:** 12.3 MB (beats 73.37%)  
**Submitted:** 2026-11-15T16:50:00.279Z  

```py
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        w1 = 0
        w2 = 0
        c1 = 0
        c2 = 0
        while w1<len(word1) and w2<len(word2):
            if word1[w1][c1] != word2[w2][c2]:
                return False
            # make characters move from 0 to 1
            c1+=1
            c2+=1

            if c1 == len(word1[w1]):
                w1+=1
                c1 = 0
            
            if c2 == len(word2[w2]):
                w2+=1
                c2 =0
            
        return w1==len(word1) and w2==len(word2)


```

---

[View on LeetCode](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/)