# Day 3: Intro to Conditional Statements

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

**Objective**	
In this challenge, we learn about conditional statements. Check out the [Tutorial](/challenges/30-conditional-statements/tutorial) tab for learning materials and an instructional video.

**Task**		
Given an integer, $n$, perform the following conditional actions:

* If $n$ is odd, print `Weird`
* If $n$ is even and in the inclusive range of $2$ to $5$, print `Not Weird`
* If $n$ is even and in the inclusive range of $6$ to $20$, print `Weird`
* If $n$ is even and greater than $20$, print `Not Weird`

Complete the stub code provided in your editor to print whether or not $n$ is weird.

**Input Format**

A single line containing a positive integer, $n$.

**Constraints**

- $ 1 \le n \le 100$

**Output Format**

Print `Weird` if the number is weird; otherwise, print `Not Weird`.

**Sample Input 0**
	
    3
    
**Sample Output 0**
	
    Weird

**Sample Input 1**
	
    24
    
**Sample Output 1**
	
    Not Weird

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-07T21:11:07.571Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if N% 2 !=0:
        print('Weird')
    elif N%2==0 and 2<= N <=5:
        print('Not Weird')
    elif N%2==0 and 6<= N <=20:
        print('Weird')
    else:
        print('Not Weird')
        

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/30-conditional-statements/problem)