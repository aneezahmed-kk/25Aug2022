#!/bin/python3

import math
import os
import random
import re
import sys


def maxMin(k, arr):
    
    results = []
    arr = sorted(arr)

    for i in range(0,(len(arr)-k +1)):
        diff = (arr[i+k-1]) - (arr[i])
        print(diff)
        results.append(diff)
    
    return (min(results))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

