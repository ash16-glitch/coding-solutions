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
**Runtime:** 3 ms (beats 55.02%)  
**Memory:** 12.9 MB (beats 81.09%)  
**Submitted:** 2026-11-14T06:02:55.508Z  

```py
class Solution(object):
    def sortArrayByParity(self, nums):
        result = []
        for i in nums:
            if i%2==0:
                result.append(i)
        for j in nums:
            if j%2!=0:
                result.append(j)
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/sort-array-by-parity/)