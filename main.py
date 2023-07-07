
import math
import os
import random
import re
import sys
from collections import defaultdict


# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    d = defaultdict(int)
    r_val = 0
    for val in a:
        d[val] += 1
        r_val = max(r_val, d[val]+d[val+1], d[val]+d[val-1])

    return r_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
