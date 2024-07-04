# Chapter : 2 - Python 2

## item : 1 - Simple OOP Calculator

จงเขียน Overloading Function สำหรับ Calculator class โดยที่มีรูปแบบ Code ดังนี้ (สามารถเพิ่มพารามิเตอร์ได้)

Skeleton Code
```
class Calculator :
	### Enter Your Code Here ###

	def __add__(self):
		###Enter Your Code For Add Number###

	def __sub__(self):
		###Enter Your Code For Sub Number###

	def __mul__(self):
		###Enter Your Code For Mul Number###

	def __truediv__(self):
		###Enter Your Code For Div Number###

x,y = input("Enter num1 num2 : ").split(",")
x,y = Calculator(int(x)),Calculator(int(y))
print(x+y,x-y,x*y,x/y,sep = "\n")
```
Test Case #1
```
Enter num1 num2 : 5,5
10
0
25
1.0
```

Test Case #2
```
Enter num1 num2 : 20,5
25
15
100
4.0
```

Test Case #3 - Hidden
Test Case #4 - Hidden

## item : 2 - weirdSubtract
จงสร้างฟังก์ชัน weirdSubstract โดยรับ parameter n,k โดยมีเงื่อนไขคือ

 - หาก n ลงท้ายด้วย 0 ให้ตัด 0 ตัวสุดท้ายทิ้ง 
 - หากไม่ใช่ ให้ทำการลดค่า n ลง 1 ค่า 
 - โดยทำซ้ำทั้งหมด k รอบ

ตัวอย่าง เช่น n = 21 , k =3
ดังนั้นทำซ้ำ 3 รอบโดย

 - รอบที่ 1 : n จะลดค่าลง 1 เหลือเป็น 20 
 - รอบที่ 2 : n จะตัด 0 ตัวสุดท้ายทิ้งเหลือเป็น 2 
  - รอบที่ 3 : n จะลดค่าลง 1 เหลือเป็น 1

ค่าที่จะ return ค่า 1 ออกมา

Skeleton Code
```
def weirdSubtract(n,k):
	### Enter Your Code Here ###
	return ...

n,s = input("Enter num and sub : ").split()
print(weirdSubtract(int(n),int(s)))
```
Test Case #1
```
Enter num and sub : 163 8
12
```

Test Case #2
```
Enter num and sub : 10 1
1
```

Test Case #3
```
Enter num and sub : 2021 5
20
```

Test Case #4
```
Enter num and sub : 2077 55
0
```

## item : 3 - New Range
ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการสร้าง range() ใหม่ขึ้นมาโดยใช้ function แค่ 1 function  

- ถ้าหากเป็น 1 argument -> range(a) | start = 0 , end = a , step = 1
- ถ้าหากเป็น 2 argument -> range(a, b) | start = a , end = b , step = 1
- ถ้าหากเป็น 3 argument -> range(a, b, c) | start = a , end = b , step = c

Test Case #1
```
*** New Range ***
Enter Input : 10
(0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)
```

Test Case #2
```
*** New Range ***
Enter Input : 3.2 6.32
(3.2, 4.2, 5.2, 6.2)
```

Test Case #3
```
*** New Range ***
Enter Input : 0.112 6.45 1.35
(0.112, 1.462, 2.812, 4.162, 5.512)
```

Test Case #4
```
*** New Range ***
Enter Input : 1 7 1.2
(1.0, 2.2, 3.4, 4.6, 5.8)
```

Test Case #5
```
*** New Range ***
Enter Input : 1.2 5.9 0.45
(1.2, 1.65, 2.1, 2.55, 3.0, 3.45, 3.9, 4.35, 4.8, 5.25, 5.7)
```
## item : 4 - nong saimai

หาค่าฐานของอายุของน้องสายไหม ที่อายุ 20,21 ตลอดกาล เช่น

- hbd(65) = "saimai is just 21, in base 32!"
- hdb(21) = "saimai is just 21, in base 10!"
- hdb(8888) = "saimai is just 20, in base 4444!"

Skeleton Code
```
def hbd(age):
	### Enter Your Code Here ###
	return ...

year = input("Enter year : ")
print(hbd(int(year)))
```

Test Case #1
```
Enter year : 555
saimai is just 21, in base 277!
```

Test Case #2
```
Enter year : 6
saimai is just 20, in base 3!
```

Test Case #3
```
Enter year : 320
saimai is just 20, in base 160!
```

## item : 5 - รหัสลับ
ตึกลึกลับแห่งหนึ่งเมื่อเดินไปข้างหลังจะมีคนบอกรหัสลับมาจงสร้างฟังชั่นคำนวณรหัส โดยรหัสจะประกอบไปด้วย english word that have repeat character เช่น bon("ball") = 48 หรือ bon("aah") = 4

Skeleton Code
```
def bon(w):
	ans = 0
	### Enter Your Code Here ###
	
	return ans
	
secretCode = input("Enter secret code : ")
print(bon(secretCode))
```

Test Case #1
```
Enter secret code : ball
48
```
Test Case #2
```
Enter secret code : ascii
36
```
Test Case #3
```
Enter secret code : daddy
16
```
Test Case #4
```
Enter secret code : press
76
```
Test Case #5 - Hidden
Test Case #6 - Hidden