def SieveOfEratosthenes(n):
    ListOfPrimes = [True for i in range(n+1)]
    ListOfPrimes[0] = False
    ListOfPrimes[1] = False
    p = 2
    while (p * p <= n):
        if (ListOfPrimes[p] == True):
            for i in range(p * p, n+1, p):
                ListOfPrimes[i] = False
        p += 1
    return ListOfPrimes

def T_Prime(arr):
    limit = int(max(arr)**(1/2))+1
    prime_list = SieveOfEratosthenes(limit)
    for target in arr:
        sqrt = target**(1/2)
        if int(sqrt) == sqrt:
            sqrt = int(sqrt)
            if prime_list[sqrt]:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')

T = int(input())
arr = input().split()
arr = [int(i) for i in arr]
T_Prime(arr)