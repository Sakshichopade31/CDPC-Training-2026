""" 
Q. 1 

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    
    sum = 0
    for i in range(len(ar)):
        sum = sum + ar[i]

    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
-----------------------------------------------------------------------
Q.2
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    
    primary = 0
    secondary = 0
    
    for i in range(n):
        primary += arr[i][i]
        secondary += arr[i][n-i-1]
        
    return abs(primary - secondary)
    
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
----------------------------------------------------------------------------
Q.3
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0 
    zero = 0
    for i in arr:
        if i > 0 :
            positive += 1 
        elif i < 0:
            negative += 1
        else:
            zero += 1
    
    print("{:.6f}".format(positive/n))
    print("{:.6f}".format(negative/n))
    print("{:.6f}".format(zero/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
-----------------------------------------------------------
"""