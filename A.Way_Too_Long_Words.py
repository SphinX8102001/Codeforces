import sys
T = int(sys.stdin.readline())
for i in range(T):
    word = sys.stdin.readline().strip()
    n = len(word)
    if n <= 10:
        output = word
    else:
        count_of_letters_apart_from_the_first_and_last = n-2
        output = word[0]+str(count_of_letters_apart_from_the_first_and_last)+word[-1]
    print(output)
