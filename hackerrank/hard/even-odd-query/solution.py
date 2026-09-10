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
