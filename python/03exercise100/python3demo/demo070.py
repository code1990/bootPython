# Python 选择排序
import sys
A=[1,2,3]
for i in range(len(A)):
    mid_idx=i
    for j in range(i+1,len(A)):
        if A[mid_idx]>A[j]:
            mid_idx=j

    A[i],A[mid_idx]=a[mid_idx],a[i]

