import sys
def is_lucky_num(num):
    while num > 0:
        last_digit = num % 10
        if last_digit != 4 and last_digit != 7:
            return False
        else:
            num = int(num//10)
    return True        

def generate_all_luckyNumbers(num):
    lucky_nums = []
    for i in range(1,num):
        if is_lucky_num(i):
            lucky_nums.append(i)
    return lucky_nums

def is_almost_lucky(num):       
    lucky_nums = generate_all_luckyNumbers(num)
    for i in lucky_nums:
        if num % i == 0:
            return True
    return False    

def main():
    UserInput = int(sys.stdin.readline().strip())
    if (is_lucky_num(UserInput)):
        print("YES")
    elif is_almost_lucky(UserInput):
        print("YES")
    else:
        print("NO")        

main()