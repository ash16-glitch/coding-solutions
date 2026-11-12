# Find Numbers with Even Number of Digits

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array `nums` of integers, return how many of them contain an  **even number**  of digits.

 

Original
Python
 **Example 1:** 

```
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

```

 **Example 2:** 

```
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.

```

 

 **Constraints:** 

- 1 <= nums.length <= 500
- 1 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 28.51%)  
**Memory:** 12.1 MB (beats 84.84%)  
**Submitted:** 2026-11-12T18:13:54.213Z  

```py
class Solution(object):
    def findNumbers(self, nums):
        counter = 0
        for i in nums:
            digit_count = 0
            while i>0:
                i//=10
                digit_count+=1
            if digit_count%2==0:
                counter+=1
        return counter
```

---

[View on LeetCode](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)