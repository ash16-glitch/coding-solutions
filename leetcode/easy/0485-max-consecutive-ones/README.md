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
**Runtime:** 36 ms (beats 36.08%)  
**Memory:** 13.4 MB (beats 77.90%)  
**Submitted:** 2026-09-28T16:51:51.411Z  

```py
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxcount = 0
        currentcounter = 0
        for num in nums:
            if num ==1:
                currentcounter +=1
                maxcount = max(maxcount,currentcounter)
            else:
                currentcounter = 0
        return maxcount

        """
        :type nums: List[int]
        :rtype: int
        """
        
```

---

[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/)