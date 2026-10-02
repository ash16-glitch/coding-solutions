# Contains Duplicate II

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums` and an integer `k`, return `true`  *if there are two  **distinct indices*** `i` *and* `j` *in the array such that* `nums[i] == nums[j]` *and* `abs(i - j) <= k`.

 

 **Example 1:** 

```
Input: nums = [1,2,3,1], k = 3
Output: true

```

 **Example 2:** 

```
Input: nums = [1,0,1,1], k = 1
Output: true

```

 **Example 3:** 

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109
- 0 <= k <= 105

## Solution

**Language:** Python  
**Runtime:** 94 ms (beats 11.49%)  
**Memory:** 26.5 MB (beats 65.84%)  
**Submitted:** 2026-10-02T20:49:22.874Z  

```py
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        windows = set()
        l = 0
        for r in range(len(nums)):
            if r-l >k:
                windows.remove(nums[l])
                l+=1
            if nums[r] in windows:
                return True

            windows.add(nums[r])
        return False
        
```

---

[View on LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)