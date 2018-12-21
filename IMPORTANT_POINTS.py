import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


def IMPORTANT_POINTS(a, R):
    minmax_list = []
    temp_1, temp_2, i = FIND_FIRST_TWO(a, R)
    minmax_list.append(temp_1)
    minmax_list.append(temp_2)
    n = len(a)
    if i < n and a[i-1] > a[0]:
        temp, i = FIND_MINIMUM(a, R, i)
        minmax_list.append(temp)
    while i < n:
        temp1, i = FIND_MAXIMUM(a, R, i)
        minmax_list.append(temp1)                              # 
        if i < n:                                              #    CHANGED   [ADDED 'if' CONDITION]
            temp2, i = FIND_MINIMUM(a, R, i)                   #
            minmax_list.append(temp2)
    return minmax_list


def FIND_FIRST_TWO(a, R):
    i = 0
    iMin = 1; iMax=1
    n = len(a)
    while i < n and a[i]/a[iMin] < R and a[iMax]/a[i] < R:
        if a[i] < a[iMin]:
            iMin = i
        if a[i] > a[iMax]:
            iMax = i
        i = i+1
    if iMin < iMax:
        return (a[iMin], iMin, 'Min'), (a[iMax], iMax, 'Max'), i
    else:
        return (a[iMax], iMax, 'Max'), (a[iMin], iMin, 'Min'), i


def FIND_MINIMUM(a, R, i):
    iMin = i
    n = len(a)
    while i < n and a[i]/a[iMin] < R:
        if a[i] < a[iMin]:
            iMin = i
        i = i+1
    return (a[iMin], iMin, 'Min'), i

def FIND_MAXIMUM(a, R, i):
    iMax = i
    n = len(a)
    while i < n and a[iMax]/a[i] < R:
        if a[i] > a[iMax]:
            iMax = i
        i = i+1
    return (a[iMax], iMax, 'Max'), i


