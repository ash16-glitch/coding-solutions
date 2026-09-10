# Even Odd Query

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an array *A* of size *N*. You are also given an integer *Q*. Can you figure out the answer to each of the *Q* queries?

Each query contains 2 integers x and y, and you need to find whether the value find(x,y) is Odd or Even:

    find(int x,int y)
	{
        if(x>y)	return 1;
        ans = pow(A[x],find(x+1,y))
        return ans
    }
    
Note : pow(a,b) = *a<sup>b</sup>*.

**Input Format**  
The first line of the input contains an integer *N*. 
The next line contains *N* space separated non-negative integers(whole numbers less than or equal to 9).  
The line after that contains a positive integer, *Q* , the denotes the number of queries to follow.
*Q* lines follow, each line contains two positive integer *x* and *y* separated by a single space.   

**Output Format**  
For each query, display 'Even' if the value returned is Even, otherwise display 'Odd'.

**Constraints**  
2 &le; *N* &le; 10<sup>5</sup>  
2 &le; *Q* &le; 10<sup>5</sup>  
1 &le; *x,y* &le; *N*  
*x* &le; *y*

Array is 1-indexed.  

*No 2 consecutive entries in the array will be zero.*

**Sample Input** 

    3
    3 2 7
    2
    1 2
    2 3

**Sample Output** 

    Odd
    Even

**Explanation**

find(1,2) = 9, which is Odd  
find(2,3) = 128, which is even

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-10T19:59:35.271Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. 2D_INTEGER_ARRAY queries
#

def solve(arr, queries):
    n = len(arr)
    # next_zero[i] = smallest index j >= i (0-indexed) such that arr[j] == 0, or n if none
    next_zero = [n] * (n + 1)
    for i in range(n - 1, -1, -1):
        next_zero[i] = i if arr[i] == 0 else next_zero[i + 1]

    result = []
    for x, y in queries:
        x0, y0 = x - 1, y - 1  # 0-indexed
        a = arr[x0]

        if a % 2 == 1:
            result.append("Odd")
        elif x0 == y0:
            result.append("Even")
        else:
            # a is even. Need to know if find(x0+1, y0) == 0.
            # That happens iff arr[x0+1] == 0 (the very next element is zero) 
            # AND x0+1 < y0 (there's still an exponent above it to make it 0^positive)
            # OR x0+1 == y0 and arr[x0+1] == 0 -> find is 0^1 = 0 still.
            # So: find(x0+1,y0) == 0 iff arr[x0+1] == 0, for x0+1 <= y0.
            if arr[x0 + 1] == 0:
                # exponent is 0 -> a^0 = 1 -> Odd
                result.append("Odd")
            else:
                result.append("Even")

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(arr, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/even-odd-query/problem)