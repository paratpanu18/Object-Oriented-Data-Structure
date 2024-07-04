#  Chapter : 1 - Python 1

##  item : 1 - radius and area of circle
เขียนโปรแกรม Python ซึ่งรับ input เป็นรัศมีของวงกลม จากนั้นคำนวณพื้นที่และแสดงผล
กำหนดให้ pi = 3.14159

Test Case #1
```
    r=1.1
    Area=3.8013239000000003
```
Test Case #2
```
    r=0
    Area=0.0
```
Test Case #3 จำนวนลบ
```
    r=-1.2
    Area=4.5238895999999995
```

Test Case #4 - Hidden
Test Case #5 - Hidden

## item : 2 - BMI Calculate
รับ input 2 จำนวนโดยที่ input ที่ 1 คือ h เป็นค่าความสูง(เมตร) และ Input ที่ 2 คือ w เป็นค่าน้ำหนัก(กิโลกรัม) โดยให้คำนวณหาค่า BMI ที่คำนวณจากสูตร BMI = w / (h^2) โดยให้แสดงผลตามข้อความข้างล่าง

 - BMI < 18.50 	แสดงผล Less Weight
 - 18.50 <= BMI < 23 แสดงผล Normal Weight 
 - 23 <= BMI < 25 แสดงผล   Morethan Normal Weight 
 - 25 <= BMI < 30 แสดงผล Getting Fat 
 - BMI >= 30 แสดงผล Fat

Test Case #1
```
    Enter your High and Weight : 1.7 70
    More than Normal Weight
```
Test Case #2
```
    Enter your High and Weight : 1.7 65
    Normal Weight
```
  Test Case #3
```
    Enter your High and Weight : 1.7 60
    Normal Weight
```
Test Case #4
```
    Enter your High and Weight : 1.85 70
    Normal Weight
```
Test Case #5
```
    Enter your High and Weight : 1.90 65
    Less Weight
```
Test Case #6
```
    Enter your High and Weight : 1.7 90
    Fat
```
Test Case #7
```
    Enter your High and Weight : 1.7 85
    Getting Fat
```
 Test Case #8
```
    Enter your High and Weight : 1.87 120
    Fat
```
## item : 3 - loop
จงเขียนโปรแกรมรับตัวเลขจำนวนเต็ม ไม่เกิน 30 หลัก แล้วหาผลรวมของเลขโดด แต่ละหลัก
-   รับตัวเลข 123 => 1+2+3=6
-   รับตัวเลข 7892 => 7+8+9+2=26
-   รับตัวเลข 32189657 => 3+2+1+8+9+6+5+7=41

Test Case #1
```
     *** Summation of each digit ***
    Enter a positive number : 123
    Summation of each digit =  6
```

Test Case #2
```
     *** Summation of each digit ***
    Enter a positive number : 7892
    Summation of each digit =  26
```

Test Case #3
```
     *** Summation of each digit ***
    Enter a positive number : 32189657
    Summation of each digit =  41
```

Test Case #4
```
     *** Summation of each digit ***
    Enter a positive number : 987654321987654321
    Summation of each digit =  90
```

Test Case #5
```
     *** Summation of each digit ***
    Enter a positive number : 9999999999333333333355555
    Summation of each digit =  145
```

Test Case #6
```
     *** Summation of each digit ***
    Enter a positive number : 111111111122222222223333333333
    Summation of each digit =  60
```

## item : 4 - Game Minesweeper
สร้างฟังก์ชันที่รับ input เป็น list(5x5) ของ # และ - โดยแต่ละแฮช (#) แทนทุ่นระเบิดและแต่ละขีด (-) แทนจุดที่ไม่มีทุ่นระเบิด ให้ return list ที่แต่ละขีดถูกแทนที่ด้วยตัวเลขที่ระบุจำนวนของทุ่นระเบิดที่อยู่ติดกับจุดนั้น (แนวนอนแนวตั้งและแนวทแยงมุม)

Skeleton Code
```
    def num_grid(lst):
	    #Code Here
	    return lst
    
    '''lst_input = [
    ["-","-","-","-","-"],
    ["-","-","-","-","-"],
    ["-","-","#","-","-"],
    ["-","-","-","-","-"],
    ["-","-","-","-","-"]
    ]'''
    
    lst_input = []
    input_list = input().split(",")
    
    for e in input_list:
	    lst_input.append([i for i in e.split()])
    
    print("\n",*lst_input,sep = "\n")
    print("\n",*num_grid(lst_input),sep = "\n")
```
Test Case #1
```
    *** Minesweeper ***
    Enter input(5x5) : - - - - -,- - - - -,- - # - -,- - - - -,- - - - -
    
    
    ['-', '-', '-', '-', '-']
    ['-', '-', '-', '-', '-']
    ['-', '-', '#', '-', '-']
    ['-', '-', '-', '-', '-']
    ['-', '-', '-', '-', '-']
    
    
    ['0', '0', '0', '0', '0']
    ['0', '1', '1', '1', '0']
    ['0', '1', '#', '1', '0']
    ['0', '1', '1', '1', '0']
    ['0', '0', '0', '0', '0']
```

Test Case #2
```
    *** Minesweeper ***
    Enter input(5x5) : - - - # -,- # - - -,- - # - -,- - - - -,- # - - -
    
    
    ['-', '-', '-', '#', '-']
    ['-', '#', '-', '-', '-']
    ['-', '-', '#', '-', '-']
    ['-', '-', '-', '-', '-']
    ['-', '#', '-', '-', '-']
    
    
    ['1', '1', '2', '#', '1']
    ['1', '#', '3', '2', '1']
    ['1', '2', '#', '1', '0']
    ['1', '2', '2', '1', '0']
    ['1', '#', '1', '0', '0']
```

Test Case #3 - Hidden
Test Case #4 - Hidden

## item : 5 - vickrey auction
จงสร้าง vickrey auction แบบจำลอง

Vickrey auction คือการประมวลที่ผู้ที่จะชนะการประมูล คือ ผู้ที่ยื่นซองเสนอราคาสูงที่สุด แต่จะจ่ายจริงในราคาที่สูงเป็นอันดับสองรองลงมา

Word:
```
    "Enter All Bid : "
    "not enough bidder"  
    "error : have more than one highest bid"
    "winner bid is $ need to pay $"
```
Test Case #1
```
    Enter All Bid : 5
    not enough bidder
```
Test Case #2
```
    Enter All Bid : 5 10 20 5 16
    winner bid is 20 need to pay 16
```
Test Case #3
```
    Enter All Bid : 5 10 20 20 10
    error : have more than one highest bid
```
Test Case #4 - Hidden