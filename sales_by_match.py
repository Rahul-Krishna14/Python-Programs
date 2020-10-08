import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 1
    pair = 0
    p = 0
    a = []
    for i in range(len(ar)):
        if ar[i] not in a:
            a.append(ar[i])
            print(a)
            for j in range(i+1,len(ar)):
                if ar[i] == ar[j]:
                    count += 1
            if count % 2 == 0:
                pair = count/2
                p += pair
            elif (count-1) % 2 ==0:
                pair = (count-1)/2
                p += pair
        count = 1
    
    return int(p)
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
