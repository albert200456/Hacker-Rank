#!/bin/python

import sys

def cancelClass(n,k,a):
    late_count = 0
    for x in a:
        if x > 0:
            late_count += 1
    present_student = n - late_count
    if  present_student >= k:
        return 'NO'
    else:
        return 'YES'

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    print cancelClass(n,k,a)
