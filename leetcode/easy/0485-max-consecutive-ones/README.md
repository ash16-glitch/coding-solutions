# Max Consecutive Ones

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a binary array `nums`, return  *the maximum number of consecutive* `1` *'s in the array*.

 

 **Example 1:** 

```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

```

 **Example 2:** 

```
Input: nums = [1,0,1,1,0,1]
Output: 2

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 45 ms (beats 11.64%)  
**Memory:** 13.7 MB (beats 43.75%)  
**Submitted:** 2026-09-28T16:43:45.006Z  

```py
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current = 0
        maxcounter = 0
        for num in nums:
            if num ==1:
                current +=1
                maxcounter = max(current, maxcounter)     
            else:
                current = 0
        return maxcounter

        """
        :type nums: List[int]
        :rtype: int
        """
        
```

---

[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/)