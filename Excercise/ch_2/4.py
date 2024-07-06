# def numberToBase(n, b):
#     if n == 0:
#         return [0]
#     digits = []
#     while n:
#         digits.append(int(n % b))
#         n //= b
#     return int("".join([str(i) for i in digits[::-1]]))

# def hbd(age):
#     result = 0
#     base = 2
#     while result != 20 and result != 21:
#         base += 1
#         result = numberToBase(age, base)
    
#     return f'saimai is just {result}, in base {base}!'

def hbd(age):
    base_result = age // 2
    actual_age_result = 20 if age % 2 == 0 else 21
    return f'saimai is just {actual_age_result}, in base {base_result}!'
year = int(input("Enter year : "))

print(hbd(int(year)))