# Sort Array By Parity

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return  ***any array**  that satisfies this condition*.

 

Original
Python
 **Example 1:** 

```
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 5000
- 0 <= nums[i] <= 5000

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 34.40%)  
**Memory:** 12.7 MB (beats 97.34%)  
**Submitted:** 2026-11-14T07:26:32.890Z  

```py
class Solution(object):
    def sortArrayByParity(self, nums):
        l = 0
        r = len(nums)-1
        while l<r:
            if nums[l]%2==0:
                l+=1
            elif nums[r]%2!=0:
                r-=1
            else:
                nums[l],nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        return nums
```

---

[View on LeetCode](https://leetcode.com/problems/sort-array-by-parity/)