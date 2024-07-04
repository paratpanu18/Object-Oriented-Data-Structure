PI = 3.141592

height, weight = input("Enter your High and Weight : ").split()
height = float(height)
weight = float(weight)

bmi = weight / height ** 2

if bmi < 18.5:
    print("Less Weight")
elif 18.5 <= bmi < 23:
    print("Normal Weight")
elif 23 <= bmi < 25:
    print("More than Normal Weight")
elif 25 <= bmi < 30:
    print("Getting Fat")
elif bmi >= 30:
    print("Fat")

