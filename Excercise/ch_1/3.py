'''
 *** Summation of each digit ***
Enter a positive number : 123
Summation of each digit =  6
'''

print(" *** Summation of each digit ***")
number = input("Enter a positive number : ")

sum = 0

for c in number:
    sum += int(c)

print("Summation of each digit = ", sum)
