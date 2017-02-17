#!/bin/python
def partition(ar):    
    p = ar[0]
    left = []
    equal = []
    right = []
    for x in ar:
        if x < p:
            left.append(x)
        elif x == p:
            equal.append(x)
        elif x > p:
            right.append(x)
    ans = left + equal + right
    return ans

m = input()
ar = [int(i) for i in raw_input().strip().split()]
output = partition(ar)
for i in output:
    print i,
