'''Decimal place correction'''
N = 5

def decimal_place(num):
    num = str(num)
    decimal_index = num.index('.')
    return len(num[decimal_index:-1])


def range(start, end, step):
    ans = []

    while start < end:
        ans.append(float(start))
        start += step

    ans_round = [round(i, 3) if decimal_place(i) >= N else i for i in ans]
    return tuple(ans_round)
    
print("*** New Range ***")
input = [float(num) for num in input("Enter Input : ").split()]

if len(input) == 1:
    print(range(0, input[0], 1))

if len(input) == 2:
    print(range(input[0], input[1], 1))

if len(input) == 3:
    print(range(input[0], input[1],input[2]))

