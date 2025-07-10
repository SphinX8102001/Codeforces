import sys
T = sys.stdin.readline().strip().split()
T = [int(x) for x in T]
n,kth_idx = T[0],T[1]
arr = sys.stdin.readline().strip().split()
arr = [int(x) for x in arr]
k = arr[kth_idx-1]
count = 0

for i in arr:
    if i>0:
        if i >= k:
            count += 1
print(count)        