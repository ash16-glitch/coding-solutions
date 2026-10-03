# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `arr` and two integers `k` and `threshold`, return  *the number of sub-arrays of size* `k` *and average greater than or equal to* `threshold`.

 

 **Example 1:** 

```
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

```

 **Example 2:** 

```
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

```

 

 **Constraints:** 

- 1 <= arr.length <= 105
- 1 <= arr[i] <= 104
- 1 <= k <= arr.length
- 0 <= threshold <= 104

## Solution

**Language:** Python  
**Runtime:** 71 ms (beats 16.84%)  
**Memory:** 20 MB (beats 22.69%)  
**Submitted:** 2026-10-03T20:59:49.699Z  

```py
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        counter = 0 # global counter to count threshold
        l = 0 # left pointer window
        maxsum = 0 # max sum of windows
        for r in range(len(arr)):
            maxsum = maxsum+arr[r]
            if r-l+1 >k:
                maxsum = maxsum - arr[l]
                l+=1 
            
            if r-l+1 == k:
                if maxsum/k >= threshold:
                    counter+=1
        return counter 
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)