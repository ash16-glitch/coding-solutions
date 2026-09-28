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
**Runtime:** 19 ms (beats 76.62%)  
**Memory:** 13.4 MB (beats 94.08%)  
**Submitted:** 2026-09-28T16:41:15.679Z  

```py
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxsum =0
        currsum = 0
        for i in nums:
            if i >0:
                currsum+=i
            if currsum>maxsum:
                maxsum = currsum
            if i ==0:
                currsum = 0
        return maxsum

        """
        :type nums: List[int]
        :rtype: int
        """
        
```

---

[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/)