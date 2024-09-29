def gcd(x, y) -> int:
    if not x and not y:
        raise ZeroDivisionError('Error! must be not all zero.')
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
x, y = [int(num) for num in input("Enter Input : ").split()]

temp_x = x
x = x if x > y else y
y = y if y < x else temp_x

try:
    print(f'The gcd of {x} and {y} is : {gcd(abs(x), abs(y))}')
except ZeroDivisionError as e:
    print(e)