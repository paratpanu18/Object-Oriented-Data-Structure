# Chapter : 3 - Stack
## item : 1 - รู้จักกับ STACK
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา <br>

A  `value` ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK <br>

P ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น -1 <br>

*** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา ถ้าหากไม่มีแล้วให้แสดงคำว่า Empty

Test Case #1
```
Enter Input : A 10,A 20,A 30,A 40,P,P
Add = 10 and Size = 1
Add = 20 and Size = 2
Add = 30 and Size = 3
Add = 40 and Size = 4
Pop = 40 and Index = 3
Pop = 30 and Index = 2
Value in Stack = 10 20
```

Test Case #2
```
Enter Input : A 10,A 20,A 30,A 40,P,A 50,A 60,P,P,P,P,P,P
Add = 10 and Size = 1
Add = 20 and Size = 2
Add = 30 and Size = 3
Add = 40 and Size = 4
Pop = 40 and Index = 3
Add = 50 and Size = 4
Add = 60 and Size = 5
Pop = 60 and Index = 4
Pop = 50 and Index = 3
Pop = 30 and Index = 2
Pop = 20 and Index = 1
Pop = 10 and Index = 0
-1
Value in Stack = Empty
```

Test Case #3 - Hidden


Test Case #4
```
Enter Input : P,A 99,P,P,A 88,P,P,A 12,A 13,A 86
-1
Add = 99 and Size = 1
Pop = 99 and Index = 0
-1
Add = 88 and Size = 1
Pop = 88 and Index = 0
-1
Add = 12 and Size = 1
Add = 13 and Size = 2
Add = 86 and Size = 3
Value in Stack = 12 13 86
```

## item : 2 - แ ต ก ดั ง เ พ ล้ ง ! ! !
กฤษฎาได้ถูกคุณแม่ไหว้วานให้ล้างจานกองเป็นภูเขา แต่ทว่ากฤษฎาก็ได้สังเกตเห็นว่าจานแต่ละใบนั้นมีน้ำหนักที่แตกต่างกัน และบนจานยังมีตัวเลขอีกด้วย กฤษฎาได้เหม่อลอยเนื่องจากครุ่นคริสว่าตัวเลขนั้นหมายถึงอะไร กฤษฎาก็ได้ทำจานหลุดมือจนจานแตก และเมื่อจานแตกได้มีเสียงที่มีความถี่ตามเลขบนจาน กฤษฎาจึงนึกสนุกได้นำจานขนาดต่างๆและมีความถี่ต่างกันมาวางซ้อนๆกัน โดยถ้าหากนำจานที่มีน้ำหนักมากกว่ามาวางบนจานที่มีน้ำหนักน้อยกว่า จะทำให้จานที่มีน้ำหนักน้อยกว่า แตก !!! และจะแตกไปเรื่อยๆจนกว่าจานใบด้านล่างจะมีน้ำหนักเท่ากันหรือมากกว่า หรือจนกว่าจะไม่มีจานด้านล่างมารองรับแล้ว <br>

ให้น้องๆเขียนโปรแกรมอ่านลำดับของจานที่กฤษฎาได้วางลงไปโดยให้ใส่จานทีละใบ ซึ่งรวมถึงขนาดของจานและความถี่ของจาน จากนั้นให้หาว่าลำดับของความถี่ของจานที่ได้ยินเมื่อวางจานลงไปตามนั้นแล้วจะเป็นเช่นใด <br>

อธิบาย Input : จะมีแค่รูปแบบเดียวคือ < a b > โดยที่ a = น้ำหนักของจาน , b = ความถี่ของจาน

Test Case #1
```
Enter Input : 1 10,5 20,3 30,3 40,4 50
10
40
30
```

Test Case #2
```
Enter Input : 90 8,68 99,44 3,44 102,50 2
102
3
```

Test Case #3 - Hidden
Test Case #4 - Hidden
Test Case #5 - Hidden

## item : 3 - Infix to Postfix
ให้รับ Input เป็น Infix และแสดงผลลัพธ์ออกมาเป็น Postfix โดยจะมี Operator 5 แบบ ได้แก่ + - * / ^ <br>

Skeleton Code: 
```python
class Stack:
	def __init__(self):
		pass
	def push(self, value):
		pass
	def pop(self):
		pass
	def size(self):
		pass
	def isEmpty(self):
		pass
		
inp = input('Enter Infix : ')
S = Stack()

print('Postfix : ', end='')

### Enter Your Code Here ###
while not S.isEmpty():
	print(S.pop(), end='')

print()
```

Test Case #1
```
Enter Infix : a+b
Postfix : ab+
```

Test Case #2
```
Enter Infix : a+b*c
Postfix : abc*+
```

Test Case #3
```
Enter Infix : a*b+c
Postfix : ab*c+
```

Test Case #4
```
Enter Infix : a+b*c-d
Postfix : abc*+d-
```

Test Case #5
```
Enter Infix : a+b*c-(d/e+f)*g
Postfix : abc*+de/f+g*-
```

Test Case #6
```
Enter Infix : A+(B*C-(D/E^F)*G)*H
Postfix : ABC*DEF^/G*-H*+
```

Test Case #7
```
Enter Infix : K+L-M*N+(O^P)*W/U/V*T+Q
Postfix : KL+MN*-OP^W*U/V/T*+Q+
```

Test Case #8
```
Enter Infix : G+A+(U-R)^I
Postfix : GA+UR-I^+
```

Test Case #9 - Hidden
Test Case #10 - Hidden

## item : 4 - Into the Woods
กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น และจะหันกลับมามอง ต้นไม้ที่เคยเดินผ่านไป <br>

ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น <br>

อธิบาย Input : A `height` แสดงถึงความสูงของต้นไม้ , B คือการหันหลังกลับมามอง <br>

อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง 4 ก่อนแล้วตามด้วย 3 แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น ต่อมาเดินไปเจอต้นไม้สูง 5 กับ ต้นไม้สูง 8 ตามลำดับ แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง 4 3 และ 5 <br>

โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง <br>

Skeleton Code: 
```python
class Stack:
	### Enter Your Code Here ###

S = Stack()
inp = input('Enter Input : ').split(',')

### Enter Your Code Here ###
```
Test Case #1
```
Enter Input : A 4,A 3,B,A 5,A 8,B
2
1
```

Test Case #2
```
Enter Input : A 8,A 3,A 2,A 6,A 2,B,A 10,B
3
1
```

Test Case #3
```
Enter Input : B,B,B,A 10,A 1,A 3,A 2,B,A 1,A 1,B,A 5,A 4,B
0
0
0
3
4
3
```

Test Case #4
```
Enter Input : A 1,A 2,A 3,A 4,B,A 3,A 2,B,A 99,A 5,B,A 4,B,A 67
1
3
2
3
```

Test Case #5
```
Enter Input : A 100,A 50,A 25,A 12,A 6,B,B,B,A 76,B,A 61,B,A 1,B,B,A 6,A 11,B
5
5
5
2
3
4
4
```

## item : 5 - ซอยตัน
ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output <br>

การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4 <br>

***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2*** <br>

*** สามารถสร้างได้มากกว่า 1 stack *** <br>

![ภาพประกอบโจทย์](data:image/png;base64,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)

Skeleton Code:
```python
class Stack:
	pass

print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
### Enter Your Code Here ###
```

Test Case #1
```
******** Parking Lot ********
Enter max of car,car in soi,operation : 5 1,2,3,4 arrive 5
car 5 arrive! : Add Car 5
[1, 2, 3, 4, 5]
```

Test Case #2
```
******** Parking Lot ********
Enter max of car,car in soi,operation : 4 1,2,3,4 arrive 5
car 5 cannot arrive : Soi Full
[1, 2, 3, 4]
```

Test Case #3
```
******** Parking Lot ********
Enter max of car,car in soi,operation : 5 1,2,3,4 arrive 1
car 1 already in soi
[1, 2, 3, 4]
```

Test Case #4
```
******** Parking Lot ********
Enter max of car,car in soi,operation : 8 1,4,6,2,3,5,8 arrive 7
car 7 arrive! : Add Car 7
[1, 4, 6, 2, 3, 5, 8, 7]
```

Test Case #5
```
******** Parking Lot ********
Enter max of car,car in soi,operation : 5 0 depart 3
car 3 cannot depart : Soi Empty
[]
```

Test Case #6
```
******** Parking Lot ********
Enter max of car,car in soi,operation : 4 1,3,2 depart 1
car 1 depart ! : Car 1 was remove
[3, 2]
```

Test Case #7
```
******** Parking Lot ********
Enter max of car,car in soi,operation : 6 2,3,5,7,8 depart 1
car 1 cannot depart : Dont Have Car 1
[2, 3, 5, 7, 8]
```

Test Case #8
```
******** Parking Lot ********
Enter max of car,car in soi,operation : 5 7,3,2,1,4 depart 7
car 7 depart ! : Car 7 was remove
[3, 2, 1, 4]
```

Test Case #9
```
******** Parking Lot ********
Enter max of car,car in soi,operation : 5 0 arrive 1
car 1 arrive! : Add Car 1
[1]
```