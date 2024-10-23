# Chapter : 6 - Recursion

## item : 1 - A2X2A
****** ห้ามใช้ For , While loop ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 ) ******* <br>

สังเกตุจาก Pattern และให้แสดงผลออกมาให้ถูกต้อง <br>

อินพุทจะมีค่าเป็น A ถึง Z โดยสามารถเป็น uppercase หรือ lowercase ก็ได้ <br>

Testcase #1
```
Enter input: A
A
```

Testcase #2
```
Enter input: B
A
AB
A
```

Testcase #3
```
Enter input: D
A
AB
ABC
ABCD
ABC
AB
A
```

Testcase #4
```
Enter input: d
A
AB
ABC
ABCD
ABC
AB
A
```

Testcase #5
```
Enter input: z
A
AB
ABC
ABCD
ABCDE
ABCDEF
ABCDEFG
ABCDEFGH
ABCDEFGHI
ABCDEFGHIJ
ABCDEFGHIJK
ABCDEFGHIJKL
ABCDEFGHIJKLM
ABCDEFGHIJKLMN
ABCDEFGHIJKLMNO
ABCDEFGHIJKLMNOP
ABCDEFGHIJKLMNOPQ
ABCDEFGHIJKLMNOPQR
ABCDEFGHIJKLMNOPQRS
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRSTU
ABCDEFGHIJKLMNOPQRSTUV
ABCDEFGHIJKLMNOPQRSTUVW
ABCDEFGHIJKLMNOPQRSTUVWX
ABCDEFGHIJKLMNOPQRSTUVWXY
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXY
ABCDEFGHIJKLMNOPQRSTUVWX
ABCDEFGHIJKLMNOPQRSTUVW
ABCDEFGHIJKLMNOPQRSTUV
ABCDEFGHIJKLMNOPQRSTU
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRS
ABCDEFGHIJKLMNOPQR
ABCDEFGHIJKLMNOPQ
ABCDEFGHIJKLMNOP
ABCDEFGHIJKLMNO
ABCDEFGHIJKLMN
ABCDEFGHIJKLM
ABCDEFGHIJKL
ABCDEFGHIJK
ABCDEFGHIJ
ABCDEFGHI
ABCDEFGH
ABCDEFG
ABCDEF
ABCDE
ABCD
ABC
AB
A
```

## item : 2 - Length of a String EXTRA

ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่) <br>

****ห้ามใช้คำสั่ง len, for, while, do while, split***** <br>

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว <br>

Skeleton Code:
```python
def length(txt):     
    #Code Here
print("\n",length(input("Enter Input : ")),sep="")
#ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้)
```

Testcase #1
```
Enter Input : hello
h*e~l*l~o*
5
```

Testcase #2
```
Enter Input : data structure is easy
d*a~t*a~ *s~t*r~u*c~t*u~r*e~ *i~s* ~e*a~s*y~
22
```

Testcase #3
```
Enter Input : *~*~*~
**~~**~~**~~
6
```

Testcase #4 - Hidden <br>
Testcase #5 - Hidden <br>

## item : 3 - GCD

เขียนโปรแกรมสำหรับหา หรม. ของเลข 2 ตัว <br>

****ห้ามใช้คำสั่ง len, for, while, do while หรือ ***** <br>

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 2 ตัว <br>

**บทนิยาม** <br>
ตัวหารร่วมมาก หรือ ห.ร.ม. (อังกฤษ: greatest common divisor: gcd) ของจำนวนเต็มสองจำนวนซึ่งไม่เป็นศูนย์พร้อมกัน คือจำนวนเต็มที่มากที่สุดที่หารทั้งสองจำนวนลงตัว

Testcase #1
```
Enter Input : 8 4
The gcd of 8 and 4 is : 4
```

Testcase #2
```
Enter Input : 10 20
The gcd of 20 and 10 is : 10
```

Testcase #3
```
Enter Input : 12 18
The gcd of 18 and 12 is : 6
```

Testcase #4
```
Enter Input : 9 7
The gcd of 9 and 7 is : 1
```

Testcase #5
```
Enter Input : 0 5
The gcd of 5 and 0 is : 5
```

Testcase #6
```
Enter Input : -6 9
The gcd of 9 and -6 is : 3
```

Testcase #7
```
Enter Input : -24 -36
The gcd of -24 and -36 is : 12
```

Testcase #8
```
Enter Input : 0 0
Error! must be not all zero.
```

Testcase #9 - Hidden <br>

Testcase #10
```
Enter Input : -11 -45
The gcd of -11 and -45 is : 1
```
Testcase #11 - Hidden <br>
Testcase #12 - Hidden <br>

## item : 4 - Perket
“เปอร์เกต์” เป็นอาหารแสนอร่อยที่ใครๆก็รู้จักกัน และแน่นอนว่าส่วนผสมย่อมเป็นสิ่งที่ต้องพิถีพิถันอย่างยิ่ง <br>

คุณมีส่วนผสมทั้งหมด N ชนิด แต่ละชนิดจะมีความเปรี้ยว S และความขม B เมื่อนำส่วนผสมมารวมกัน ความเปรี้ยว ลัพธ์ จะได้จากผลคูณของค่าความเปรี้ยวของทุกชนิดที่ใช้ ในขณะที่ความขมลัพธ์ จะได้จากผลบวกของความขมของ ทุกชนิดที่ใช้ ส่วนผสมที่ใช้นั้น <br>

เปอร์เกต์ที่อร่อยที่สุดนั้น จะมีผลต่างค่าความเปรี้ยวลัพธ์และค่าความขมลัพธ์ของส่วนผสมทั้งหมดน้อยที่สุด และเรา จำเป็นต้องใช้ส่วนผสมอย่างน้อย 1 ชนิด <br>

โจทย์ จงเขียนโปรแกรมเพื่อหาค่าผลต่างของความเปรี้ยวลัพธ์และความขมลัพธ์ของส่วนผสม ที่น้อยที่สุด <br>

******* อธิบาย input <br>

โดยส่วนผสมแต่ละชนิดจะแบ่งด้วย comma ( ' , ' ) โดยในแต่ละส่วนผสม จะมีจำนวนเต็มสองจำนวน S และ B คือค่าความเปรี้ยวและค่าความขมของ ส่วนผสมชนิดนั้น <br>

******* รับประกันว่าสำหรับทุกข้อมูลนำเข้า เมื่อนำส่วนผสมทุกชนิดแล้ว จะได้ค่าความเปรี้ยวลัพธ์และความขมลัพธ์ ไม่เกิน 1,000,000,000 <br>

Testcase #1
```
Enter Input : 3 10
7
```

Testcase #2
```
Enter Input : 3 8,5 8
1
```

Testcase #3
```
Enter Input : 1 7,2 6,3 8,4 9
1
```

Testcase #4 - Hidden <br>
Testcase #5 - Hidden <br>
Testcase #6 - Hidden <br>

## item : 5 - ดาวเคราะห์น้อย

นักศึกษาจะได้รับ Input เป็น list (int) ของดาวเคราะห์น้อย
สำหรับดาวเคราะห์น้อยแต่ละดวงนั้น ค่าสัมบูรณ์ จะแสดงขนาดของมัน และเครื่องหมายแสดงถึงทิศทางของมัน (ถ้าเลขเป็น**บวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย**) โดยที่ดาวเคราะห์น้อยแต่ละดวงเคลื่อนที่ด้วยความเร็วเท่ากัน <br>

ค้นหาสถานะของดาวเคราะห์น้อยหลังจากการชนกันทั้งหมด <br>

1.หากดาวเคราะห์น้อยสองดวงมาพบกันดวงที่เล็กกว่าจะระเบิด <br>

2.ถ้าทั้งสองมีขนาดเท่ากันทั้งคู่จะระเบิด <br>

3.ดาวเคราะห์น้อยสองดวงที่เคลื่อนที่ไปในทิศทางเดียวกันจะไม่มีวันพบกัน <br>

****ห้ามใช้คำสั่ง for, while, do while***** <br>

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว<br>

Skeleton Code:
```python
def asteroid_collision(asts):
    #Code Here

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))
```

Testcase #1
```
Enter Input : -2, -1, 1, 2
[-2, -1, 1, 2]
```

Testcase #2
```
Enter Input : -2, 1, 1, -2
[-2, -2]
```

Testcase #3
```
Enter Input : 1, 1, -2, -2
[-2, -2]
```

Testcase #4
```
Enter Input : 10, 2, -5
[10]
```

Testcase #5
```
Enter Input : 8, -8
[]
```

Testcase #6
```
Enter Input : 2,-2,3,4
[3, 4]
```

Testcase #7
```
Enter Input : 4,2,3,-3
[4, 2]
```

Testcase #8
```
Enter Input : -10, 66, -56, -9, -32, -41, 81, 10, 31, 65, -84, -73, -63, 94, -100, -56, -88, 41, 44, -45, -61, 12, 27, 85, -69, -26, -74, -18, -60, 90
[-10, -84, -73, -63, -100, -56, -88, -45, -61, 12, 27, 85, 90]
```

Testcase #9
```
Enter Input : 50, -36, 4, 35, 43, 72, -46, 68, 65, 94, -11, -78, -59, 15, -9, 1, 96, 42, 34, 60, -42, 5, 92, -55, 26, 39, -80, -18, -87, -51, 91, -21, -7, 80, -12, -61, -32, 6, -52, -67, 46, 24, -70, -64, -94
[50, 4, 35, 43, 72, 68, 65, 94, 15, 1, 96]
```