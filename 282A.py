import sys
X = 0

T = int(sys.stdin.readline().strip())
for i in range(T):
    user_input = sys.stdin.readline().strip()
    if '++' in user_input:
        X+=1
    elif '--' in user_input:
        X-=1
print(X)            