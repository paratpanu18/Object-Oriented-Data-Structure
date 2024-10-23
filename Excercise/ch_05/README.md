# Chapter : 4 - Queue

## item : 1 - Locomotive-(101)

มีรถไฟอยู่ขบวนหนึ่ง โดยรถไฟนั้นจะมีหมายเลขกำกับตู้แต่ละตู้อยู่และรถไฟก็มีหัวรถจักรอยู่ แต่หัวรถจักรดันไปต่อกับตู้รถไฟอยู่ พี่ต้องการให้น้อง ๆ ทำการแบ่งขบวนรถไฟออก โดยให้หัวรถจักรอยู่ข้างหน้าสุด และส่วนตู้ที่เหลือให้ทำการต่อกับตู้สุดท้ายโดยไม่มีการเปลี่ยนลำดับของตู้ <br>

ซึ่งพี่จะให้หมายเลข 0 แทนเป็นหัวรถจักร ส่วน หมายเลขอื่นจะเป็นตู้รถไฟ <br>

เช่น `2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6` <br>

เป็น `0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1` ( ให้ใช้ singly linked list)

Testcase #1
```
 *** Locomotive ***
Enter Input : 2 3 1 0 4 5 6
Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1
```

Testcase #2
```
 *** Locomotive ***
Enter Input : 5 4 3 2 1 0 9 8 7 6
Before : 5 <- 4 <- 3 <- 2 <- 1 <- 0 <- 9 <- 8 <- 7 <- 6
After : 0 <- 9 <- 8 <- 7 <- 6 <- 5 <- 4 <- 3 <- 2 <- 1
```

Testcase #3
```
 *** Locomotive ***
Enter Input : 1 0
Before : 1 <- 0
After : 0 <- 1
```

Testcase #4
```
 *** Locomotive ***
Enter Input : 0 1 2 3 4 5 6 7 8 9
Before : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9
After : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9
```

Testcase #5 - Hidden <br>

Testcase #6
```
 *** Locomotive ***
Enter Input : 1 2 3 0
Before : 1 <- 2 <- 3 <- 0
After : 0 <- 1 <- 2 <- 3
```

Testcase #7
```
 *** Locomotive ***
Enter Input : 2 0 1
Before : 2 <- 0 <- 1
After : 0 <- 1 <- 2
```

## item : 2 - รู้จักกับ Doubly Linked List

ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้

- 1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
- 2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
- 3. reverse     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่ท้ายไปจนหัวมีตัวอะไรบ้าง
- 4. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
- 5. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
- 6. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
- 7. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
- 8. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
- 9. size           คืนค่าเป็นขนาดของ Linked List
- 10. pop         นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range
- 11. insert       เป็นการนำ Item ไปแทรกใน Linked List ตามตำแหน่ง pos ไม่มีการคืนค่า

ถ้าน้องยังไม่ค่อยเข้าใจการทำงานของ insert ให้น้องลองกับ List บน Python ได้  เช่น

- 1.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(0,"T") จะได้ผลลัพธ์คือ [ "T", 0 , 1 , 2 , 3 ]
- 2.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(999,"T") จะได้ผลลัพธ์คือ [ 0 , 1 , 2 , 3 , "T" ]
- 3.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(-2,"T") จะได้ผลลัพธ์คือ [ 0 , 1 , "T" , 2 , 3 ]  
- 4.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(-10,"T") จะได้ผลลัพธ์คือ [ "T", 0 , 1 , 2 , 3 ]

โดยรูปแบบ Input มีดังนี้

- 1. append    ->  AP
- 2. addHead  ->  AH
- 3. search      ->  SE
- 4. index        ->   ID
- 5. size          ->   SI
- 6. pop          ->   PO
- 7. insert       ->   IS

โดยให้เพิ่มเติมจากส่วน #Code Here ของโปรแกรมต่อไปนี้ เพื่อให้สามารถแสดงผลได้ตามที่โจทย์กำหนด <br>
********  ห้ามใช้ List ในการทำ Linked List เด็ดขาดถ้าหากพบจะถูกลดเป็น 0 คะแนน ********

Skeleton Code:
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        #Code Here

    def addHead(self, item):
        #Code Here

    def insert(self, pos, item):
        #Code Here

    def search(self, item):
        #Code Here

    def index(self, item):
        #Code Here

    def size(self):
        #Code Here

    def pop(self, pos):
        #Code Here

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
```

Testcase #1
```
Enter Input : AP I,AP Love,AP KMITL,AP 2020
Linked List : I Love KMITL 2020 
Linked List Reverse : 2020 KMITL Love I 
```

Testcase #2
```
Enter Input : PO -999,PO 999,PO 0,AP KMITL,PO 999,PO 0
Out of Range | Empty
Out of Range | Empty
Out of Range | Empty
Out of Range | KMITL 
Success | KMITL -> Empty
Linked List : Empty
Linked List Reverse : Empty
```

Testcase #3
```
Enter Input : SI,AH 2020,SI,AH KMITL,SI,AH LOVE,SI,AH I,SI
Linked List size = 0 : Empty
Linked List size = 1 : 2020 
Linked List size = 2 : KMITL 2020 
Linked List size = 3 : LOVE KMITL 2020 
Linked List size = 4 : I LOVE KMITL 2020 
Linked List : I LOVE KMITL 2020 
Linked List Reverse : 2020 KMITL LOVE I 
```

Testcase #4
```
Enter Input : SI,IS 0 KMITL,SI,SE 0,SE KMITL,ID 0,ID KMITL,PO 0,SI,IS -999 CE,SI
Linked List size = 0 : Empty
Linked List size = 1 : KMITL 
Not Found 0 in KMITL 
Found KMITL in KMITL 
Index (0) = -1 : KMITL 
Index (KMITL) = 0 : KMITL 
Success | KMITL -> Empty
Linked List size = 0 : Empty
Linked List size = 1 : CE 
Linked List : CE 
Linked List Reverse : CE 
```

Testcase #5
```
Enter Input : AP 0,AP 1,AP 2,AP 3,SI,IS -1 KMITL,SI,ID KMITL
Linked List size = 4 : 0 1 2 3 
Linked List size = 5 : 0 1 2 KMITL 3 
Index (KMITL) = 3 : 0 1 2 KMITL 3 
Linked List : 0 1 2 KMITL 3 
Linked List Reverse : 3 KMITL 2 1 0 
```

Testcase #6
```
Enter Input : AP 0,AP 1,AP 2,AP 3,SI,IS 999 KMITL,SI
Linked List size = 4 : 0 1 2 3 
Linked List size = 5 : 0 1 2 3 KMITL 
Linked List : 0 1 2 3 KMITL 
Linked List Reverse : KMITL 3 2 1 0 
```

Testcase #7
```
Enter Input : AH 3,AH 2,AH 1,AH 0,SI,IS -3 KMITL,SI
Linked List size = 4 : 0 1 2 3 
Linked List size = 5 : 0 KMITL 1 2 3 
Linked List : 0 KMITL 1 2 3 
Linked List Reverse : 3 2 1 KMITL 0 
```

Testcase #8
```
Enter Input : AP 0,AP 1,AP 2,AP 3,SI,IS -999 KMITL,SI
Linked List size = 4 : 0 1 2 3 
Linked List size = 5 : KMITL 0 1 2 3 
Linked List : KMITL 0 1 2 3 
Linked List Reverse : 3 2 1 0 KMITL 
```

Testcase #9 - Hidden <br>
Testcase #10 - Hidden <br>

## item : 3 - Arthur กับเมืองลี้ลับ

Arthur เป็นเด็กหนุ่มผู้หลงใหลในการเขียนโปรแกรมและการแก้ปริศนา หนึ่งวันหนึ่ง เขาได้รับ จดหมายลึกลับที่บอกว่าเขาถูกเชิญให้ไปที่เมืองปริศนา ซึ่งเป็นเมืองที่ถูกสร้างขึ้นมาจากโครงสร้างข้อมูล แบบ Linked List ทั้งหมด <br>


เมื่อ Arthur มาถึงเมืองปริศนา เขาพบว่าที่นี่มีการจัดการแข่งขันเขียนโปรแกรม โดยมีเป้าหมายคือ การแก้ปริศนาและช่วยเหลือผู้อยู่อาศัยในเมืองปริศนาให้พ้นจากปัญหาต่างๆ ที่เกิดขึ้นจากโครงสร้าง ข้อมูลที่ซับซ้อน Arthur ได้รับภารกิจแรกคือการแก้ปัญหาการจัดเรียงข้อมูลใน Linked List เพื่อทำให้ข้อมูลเรียงลำดับถูกต้อง <br>

ระดับความยาก : ง่ายคดๆ <br>

หมายเหตุ:

- หลักการจัดวางคือ ตัวเลข, ตัวอักษรพิมพ์ใหญ่, ตัวอักษรพิมพ์เล็ก (คุ้นๆไหมมันคืออะไร?)
- ไม่อนุญาตให้ใช้ .sort() เพราะตรวจ code นะจ๊ะ

Testcase #1
```
Enter unsorted Linked List: 5 4 3 2 1 0
Before: 5 -> 4 -> 3 -> 2 -> 1 -> 0
After : 0 -> 1 -> 2 -> 3 -> 4 -> 5
```

Testcase #2
```
Enter unsorted Linked List: 9 3 2 90 2 -1 3 8 2 3
Before: 9 -> 3 -> 2 -> 90 -> 2 -> -1 -> 3 -> 8 -> 2 -> 3
After : -1 -> 2 -> 2 -> 2 -> 3 -> 3 -> 3 -> 8 -> 9 -> 90
```

Testcase #3 - Hidden <br>

Testcase #4
```
Enter unsorted Linked List: z x y a c b
Before: z -> x -> y -> a -> c -> b
After : a -> b -> c -> x -> y -> z
```

Testcase #5
```
Enter unsorted Linked List: A g W Z b a P Q Y i l
Before: A -> g -> W -> Z -> b -> a -> P -> Q -> Y -> i -> l
After : A -> P -> Q -> W -> Y -> Z -> a -> b -> g -> i -> l
```

Testcase #6
```
Enter unsorted Linked List: settle nationalism note technique persist herd sculpture heat flatware jury
Before: settle -> nationalism -> note -> technique -> persist -> herd -> sculpture -> heat -> flatware -> jury
After : flatware -> heat -> herd -> jury -> nationalism -> note -> persist -> sculpture -> settle -> technique
```

Testcase #7 - Hidden <br>
Testcase #8 - Hidden <br>

## item : 4 - หา loop ใน linked list

ให้ตรวจสอบว่า linked list มีการวนซ้ำหรือไม่ และ แสดงผลลัพธ์ตามตัวอย่าง <br>

โดยมีการรับ input ดังนี้

1. append ->   A <int> คือ เพิ่มข้อมูลต่อท้าย linked list
2. set_next -> S <index1(int):index2(str)> คือการ set node.next ของ node index ที่1 ให้ชี้ไป node index ที่2

ซึ่งหากไม่มี  node index ที่1 ใน linked list ให้แสดง error และหากไม่มี node index ที่2 ใน linked list ให้ทำการ append nodeใหม่เข้าไปใน linked list โดยมี value = index2

Testcase #1
```
Enter input : A 0,A 1,S 2:0
0
0->1
Error! {index not in length}: 2
No Loop
0->1
```

Testcase #2
```
Enter input : A 0,A 1,S 0:2
0
0->1
index not in length, append : 2
No Loop
0->1->2
```

Testcase #3
```
Enter input : A 0,A 1,S 1:0
0
0->1
Set node.next complete!, index:value = 1:1 -> 0:0
Found Loop
```

Testcase #4
```
Enter input : S 0:0
Error! {list is empty}
No Loop
Empty
```

Testcase #5
```
Enter input : A 0,A 3,A 5,A 7,A 9,S 2:0
0
0->3
0->3->5
0->3->5->7
0->3->5->7->9
Set node.next complete!, index:value = 2:5 -> 0:0
Found Loop
```

Testcase #6
```
Enter input : A 0,A 1,A 2,S 0:2
0
0->1
0->1->2
Set node.next complete!, index:value = 0:0 -> 2:2
No Loop
0->2
```

Testcase #7
```
Enter input : S 0:0,A 0,A 0,A 0,S 0:5,S 0:3,A 5,S 2:1
Error! {list is empty}
0
0->0
0->0->0
index not in length, append : 5
Set node.next complete!, index:value = 0:0 -> 3:5
0->5->5
Set node.next complete!, index:value = 2:5 -> 1:5
Found Loop
```

Testcase #8
```
Enter input : S 0:0,A 0
Error! {list is empty}
0
No Loop
0
```

Testcase #9 - Hidden <br>
Testcase #10 - Hidden <br>
Testcase #11 - Hidden <br>

## item : 5 - แม่งูเอ๋ย กินน้ำบ่อไหน?

เเม่งูเอ๋ยกินน้ำบ่อไหน กินน้ำบ่อทราย ย้ายไปก็ย้ายมา~ <br>


แม่งูต้องการสอนลูกงูเล่นให้รู้จักกับ linked-list โดยทำการนัดกับพ่องูให้เล่นเกมงูกินหางด้วยกัน โดยแม่งูจะเรียกลูกงูให้มาเกาะแม่งูกันเป็นเส้นตรง และให้งูทุกตัวแสดงน้ำหนักตัวเอง (แม่งูจะอยู่หัวเสมอ) ต่อมาแม่งูได้สอนการละเล่นงูกินหาง ให้ลูกงูดังนี้ <br>


ถ้าพ่องูร้องว่า “กินน้ำบ่อไหน” และถ้าแม่งูตอบว่า


- **“กินน้ำบ่อทราย ย้ายไปก็ย้ายมา”**  เมื่อลูกงูได้ยินคำสั่ง “ย้ายไปก็ย้ายมา” ให้ลูกงูที่เกาะเเม่งูอยู่นั้นสลับตำแหน่งเลขคู่เลขคี่กัน (1->2, 2->1) (ระวังลูกงูสับสน)


- **“กินน้ำบ่อโศก โยกไปก็โยกมา”** เมื่อลูกงูได้ยินคำสั่ง “โยกไปก็โยกมา”  ให้ลูกงูโยก แต่เผอิญว่าแม่งูก็โยกเช่นกัน และโยกแรงเกิน ทำให้ลูกงูที่มีขนาดเล็กกว่าแม่งูนั้นหลุดออกจากวงไป โดยลูกงูที่หลุดออกจากขบวน จะมานั่งดูแม่งูและลูกคนอื่นๆเล่นเกมต่อไป (แสดงตัวเลขที่หลุดออกจาก  linked-list)


- **“กินน้ำบ่อหิน บินไปก็บินมา”**  “บินไปก็บินมา” เป็นคำสั่งที่ให้แม่งูติดปีกบินไปขโขยลูกงูชาวบ้านมา โดยลูกงูที่แม่งูขโมยมาให้ไปต่อท้ายลูกงูตัวสุดท้ายในขบวนตลอด (แสดงตัวเลขที่แม่งูไปขโมยมาด้วย)


- **“กินหัวกินหาง กินกลางตลอดตัว”** “กินกลางตลอดตัว” เป็นคำสั่งที่ให้แม่งูและลูกงูเตรียมพร้อมรับแรงกระแทกจากพ่องู
    - โดยหากน้ำหนักของแม่งูและลูกงูรวมกันน้อยกว่าพ่องู แม่งูต้องเสียลูกงูจนกว่า พ่องูจะเจอลูกงูที่มีขนาดที่หารขนาดพ่องูลงตัว (ขนาดพ่องู mod ขนาดลูกงู = 0) 
    - แต่หากไม่มีลูกงูตัวไหนที่หารน้ำหนักพ่องูได้เลย แม่งูจึงตัดสินใจสลับหัว-หางกับลูกตัวเอง 
    - (0 เป็นลูกรัก แม่งูจะไม่ให้ตัวนี้ไปหารกับพ่องูเด็ดขาด)

โดยลูกงูที่หลุดออกจากขบวน จะมานั่งดูแม่งูและลูกคนอื่นๆเล่นเกมต่อไป (แสดงตัวเลขที่หลุดออกจาก  linked-list)


**แม่งูจะตายหากไม่มีลูกงูเกาะแม่งูอยู่เลย แม้ว่าคำสั่งต่อมาจะบอกให้แม่งูบินไปขโมยลูกงูมาก็ตาม**

**คำสั่ง:**

- บันทัดแรกแรกจะเป็นการรับตัวเลขเพื่อสร้างครอบครัวงู และรับคำสั่ง 

เช่น 	Snake family : 10 9 8 7 (แม่งูคือ 10, และมีลูกงูได้แก่ 9 8 7) 

	(10)->9->8->7

- บรรทัดต่อมาจะเป็นการรับคำสั่ง โดย

“ย้ายไปก็ย้ายมา” : SW

“โยกไปก็โยกมา” : SH

“บินไปก็บินมา” : F {input}

“กินกลางตลอดตัว” : D {input}

เช่น 	
```
Snake Game : 10 9 8 7/D 7,SH,SW,F 8
	(10)->9->8->7 
```
    
(แม่งูคือ 10, และมีลูกงูได้แก่ 9 8 7) 
จะเป็นการเล่นกับพ่องูที่มีขนาดเท่ากับ 7, แม่งูโยก, ลูกสลับตำแหน่ง, แม่งูขโมยลูกงูที่มีขนาด 8 ตามลำดับ

Testcase #1
```
Snake Game : 10 9 8 7/D 7,SH,SW,F 8
(10)->9->8->7
Play success!->[]
(10)->9->8->7
------------------------------
Shake success!->[]
(10)->9->8->7
------------------------------
Swap success!
(10)->8->9
------------------------------
Steal success!->8
(10)->8->9->8
------------------------------
Snake Game : 
```

Testcase #2
```
Snake Game : 5 1 2 3 4 5 6 7 8 9 10/SW,SH,F 4,D 63
(5)->1->2->3->4->5->6->7->8->9->10
Swap success!
(5)->2->1->4->3->6->5->8->7->10->9
------------------------------
Shake success!->[6, 8, 7, 10, 9]
(5)->2->1->4->3->5
------------------------------
Steal success!->4
(5)->2->1->4->3->5->4
------------------------------
Play success!->[5, 4]
(5)->2->1->4->3
------------------------------
Snake Game : 
```

Testcase #3
```
Snake Game : 10 5 7 3/SH,SH,SW,SW,D 44
(10)->5->7->3
Shake success!->[]
(10)->5->7->3
------------------------------
Shake success!->[]
(10)->5->7->3
------------------------------
Swap success!
(10)->7->5
------------------------------
Swap success!
(10)->5->7
------------------------------
Play success!->[]
(7)->5->10
------------------------------
Snake Game : 
```

Testcase #4
```
Snake Game : 1 2 3/SH,D 99,SW
(1)->2->3
Shake success!->[2, 3]
(1)->Empty
------------------------------
Mom is dead
Snake Game : 
```

Testcase #5
```
Snake Game : 4 0 0/F 8,F 7,F 6,D 71,D 122,D 77,D 88,SW,D 31
(4)->0->0
Steal success!->8
(4)->0->0->8
------------------------------
Steal success!->7
(4)->0->0->8->7
------------------------------
Steal success!->6
(4)->0->0->8->7->6
------------------------------
Play success!->[]
(6)->0->0->8->7->4
------------------------------
Play success!->[]
(4)->0->0->8->7->6
------------------------------
Play success!->[6]
(4)->0->0->8->7
------------------------------
Play success!->[7]
(4)->0->0->8
------------------------------
Swap success!
(4)->0->0
------------------------------
Play success!->[]
(0)->0->4
------------------------------
Snake Game : 
```

Testcase #6
```
Snake Game : -4 -3 -2 -1 0/SW,F 0,F 0,F 0,D 0,D 0,SW,SH
(-4)->-3->-2->-1->0
Swap success!
(-4)->-2->-3->0->-1
------------------------------
Steal success!->0
(-4)->-2->-3->0->-1->0
------------------------------
Steal success!->0
(-4)->-2->-3->0->-1->0->0
------------------------------
Steal success!->0
(-4)->-2->-3->0->-1->0->0->0
------------------------------
Play success!->[0, 0, 0]
(-4)->-2->-3->0->-1
------------------------------
Play success!->[]
(-4)->-2->-3->0->-1
------------------------------
Swap success!
(-4)->-3->-2->-1->0
------------------------------
Shake success!->[-3, -2, -1, 0]
(-4)->Empty
------------------------------
Mom is dead
Snake Game : 
```

Testcase #7
```
Snake Game : 7 8 9/F 10,SW,SW,SH
(7)->8->9
Steal success!->10
(7)->8->9->10
------------------------------
Swap success!
(7)->9->8
------------------------------
Swap success!
(7)->8->9
------------------------------
Shake success!->[8, 9]
(7)->Empty
------------------------------
Mom is dead
```

Testcase #8 - Hidden <br>

Testcase #9
```
Snake Game : 9 9 9 9 9/SH,F -100,D 101,D -40,F -100,SW,SH,D -20,SH,SW
(9)->9->9->9->9
Shake success!->[]
(9)->9->9->9->9
------------------------------
Steal success!->-100
(9)->9->9->9->9->-100
------------------------------
Play success!->[]
(-100)->9->9->9->9->9
------------------------------
Play success!->[]
(9)->9->9->9->9->-100
------------------------------
Steal success!->-100
(9)->9->9->9->9->-100->-100
------------------------------
Swap success!
(9)->9->9->9->9->-100->-100
------------------------------
Shake success!->[]
(9)->9->9->9->9->-100->-100
------------------------------
Play success!->[]
(-100)->9->9->9->9->-100->9
------------------------------
Shake success!->[9, 9, 9, 9, 9]
(-100)->-100
------------------------------
Swap success!
(-100)->Empty
------------------------------
Mom is dead
Snake Game :
```

Testcase #10 - Hidden <br>