#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    len_s = len(s)
    num_str = n//len_s
    rem = n%len_s

    c1 = 0
    c2 = 0

    for i in range(len_s):
        if s[i] == 'a':
            c1 += 1
        
        if s[i] == 'a' and rem > i:
            c2 += 1
    
    total = c1*num_str + c2

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
