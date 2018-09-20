#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    n = len(arr)
    options = []    
    for i in range(n):
        rest_sum = 0
        for ii in range(n):
            if i != ii:
                rest_sum = rest_sum + arr[ii]
        options.append(rest_sum)

    print(min(options), end=' ')
    print(max(options))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

# code passed all test cases.
