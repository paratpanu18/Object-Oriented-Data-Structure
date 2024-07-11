def weirdSubtract(n,k):

    for iteration in range(k):
        '''In case of last digit is 0'''
        if n % 10 == 0:
            n /= 10
            continue

        else:
            n -= 1

    return int(n)

n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))