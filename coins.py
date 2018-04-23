
import sys
import os

memodict = {1 : 1 , 0 : 0}

def bytelandian(data):
    if(data in memodict.keys()):return memodict[data]
    else:
        val = max(data , (bytelandian(data/2) + bytelandian(data/3) + bytelandian(data/4) ))
        memodict[data] = val
        return val

while True:
    try:
        print bytelandian(input())
    except:
        break

