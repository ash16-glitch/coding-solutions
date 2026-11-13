# Monotonic Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

An array is  **monotonic**  if it is either monotone increasing or monotone decreasing.

An array `nums` is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An array `nums` is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given an integer array `nums`, return `true` *if the given array is monotonic, or* `false` *otherwise*.

 

Original
Python
 **Example 1:** 

```
Input: nums = [1,2,2,3]
Output: true

```

 **Example 2:** 

```
Input: nums = [6,5,4,4]
Output: true

```

 **Example 3:** 

```
Input: nums = [1,3,2]
Output: false

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -105 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 74 ms (beats 48.29%)  
**Memory:** 20.6 MB (beats 30.67%)  
**Submitted:** 2026-11-13T19:35:06.283Z  

```py
class Solution(object):
    def isMonotonic(self, nums):
        inc = True
        dec = True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                inc = False
            if nums[i]<nums[i+1]:
                dec = False
        return inc or dec
```

---

[View on LeetCode](https://leetcode.com/problems/monotonic-array/)