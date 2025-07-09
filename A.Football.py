def Count(key,start,char):
    count = 0
    for i in range(start,len(key)):
        if key[i] == char:
            count += 1
        else:
            return count
    return count
def find_danger(key):
    L = []
    for i in range(len(key)):
        char = key[i]
        start = i
        count = Count(key,start,char)
        L.append(count)
    if 7 in L:
        print('YES')
    else:
        print('NO')

key = input()
find_danger(key)
