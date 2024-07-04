def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return int("".join([str(i) for i in digits[::-1]]))

def hbd(age):
    result = 0
    base = 2
    while result != 20 and result != 21:
        base += 1
        result = numberToBase(age, base)
    
    return f'saimai is just {result}, in base {base}!'

year = int(input("Enter year : "))

print(hbd(int(year)))