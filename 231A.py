import sys
T = int(sys.stdin.readline())
arr = []
output = 0 #count of times 2 or 3 friends agreed to solve a problem
for i in range(T):
    user_input = sys.stdin.readline().strip().split()
    one_count = 0
    for i in range(3):
        if user_input[i] == '1':
            one_count +=1
    if one_count >= 2:
        output += 1
print(output)        