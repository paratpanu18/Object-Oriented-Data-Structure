def weirdSubtract(n,k):

    for _ in range(k):
        if n % 10 == 0:
            n /= 10
        else:
            n -= 1

    return int(n)

n,s = [int(number) for number in input("Enter num and sub : ").split()]

print(weirdSubtract(n, s))