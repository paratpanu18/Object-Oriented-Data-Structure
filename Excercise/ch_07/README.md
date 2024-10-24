# Chapter : 7 - Tree 1 (Binary Search Tree)

## item : 1 - รู้จักกับ Binary Search Tree

ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

Skeleton Code:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
```

Testcase #1
```
Enter Input : 10 4 20 1 5
      20
 10
           5
      4
           1
```

Testcase #2
```
Enter Input : 4 10 3 6 13 9
           13
      10
                9
           6
 4
      3
```

Testcase #3
```
Enter Input : 1 2 3 4 5 6 7 8 0 -1 -2
                                    8
                               7
                          6
                     5
                4
           3
      2
 1
      0
           -1
                -2
```

Testcase #4 - Hidden

## item : 2 - หาค่า Below

ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยกว่าค่าที่รับเข้ามาของ Binary Search Tree

***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()

Testcase #1
```
Enter Input : 10 4 20 1 5|1
      20
 10
           5
      4
           1
--------------------------------------------------
Below 1 : Not have
```

Testcase #2
```
Enter Input : 4 10 2 1 3 7 -1 -4 9|5
      10
                9
           7
 4
           3
      2
           1
                -1
                     -4
--------------------------------------------------
Below 5 : -4 -1 1 2 3 4 
```

Testcase #3
```
Enter Input : 1 2 3 4 5 6 7 9 8 0 -1 -2|4
                                    9
                                         8
                               7
                          6
                     5
                4
           3
      2
 1
      0
           -1
                -2
--------------------------------------------------
Below 4 : -2 -1 0 1 2 3 
```

Testcase #4
```
Enter Input : 100 70 200 34 80 300|71
           300
      200
 100
           80
      70
           34
--------------------------------------------------
Below 71 : 34 70 
```

Testcase #5
```
Enter Input : 5 3 7 2 1 4 6 8|-5
           8
      7
           6
 5
           4
      3
           2
                1
--------------------------------------------------
Below -5 : Not have
```

## item : 3 - พ่อจ๋าอยู่ไหน

ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

และให้หา พ่อ(father node) ของ node ที่กำหนด

Skeleton Code:
```python
class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(r,data):
    #code here

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)
print(father(tree.root,data[1]))
```

Testcase #1
```
Enter Input : 4 3 1 2 7 6 8/1
           8
      7
           6
 4
      3
                2
           1
3
```

Testcase #2
```
Enter Input : 3 2 1 5 4 7/3
           7
      5
           4
 3
      2
           1
None Because 3 is Root
```

Testcase #3
```
Enter Input : 1 2 3/4
           3
      2
 1
Not Found Data
```

Testcase #4 - Hidden <br>
Testcase #5 - Hidden <br>
Testcase #6 - Hidden <br>

## item : 4 - สนุกไปกับ Binary Search Tree

ให้น้องรับ input เข้ามาและสร้าง Binary Search Tree ต่อมาให้แสดงผลแบบ Preorder , Inorder , Postorder และ Breadth First Search ตามลำดับ

Testcase #1
```
Enter Input : 10 4 20 1 5
Preorder : 10 4 1 5 20 
Inorder : 1 4 5 10 20 
Postorder : 1 5 4 20 10 
Breadth : 10 4 20 1 5 
```

Testcase #2
```
Enter Input : 0 -50 50 25 -25 13 -13 28 -38 75 -75 62 -62 100 -100
Preorder : 0 -50 -75 -100 -62 -25 -38 -13 50 25 13 28 75 62 100 
Inorder : -100 -75 -62 -50 -38 -25 -13 0 13 25 28 50 62 75 100 
Postorder : -100 -62 -75 -38 -13 -25 -50 13 28 25 62 100 75 50 0 
Breadth : 0 -50 50 -75 -25 25 75 -100 -62 -38 -13 13 28 62 100 
```

Testcase #3 - Hidden <br>
Testcase #4 - Hidden <br>

## item : 5 - Expression Tree

ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /

Testcase #1
```
Enter Postfix : ab+cde+**
Tree :
                e
           +
                d
      *
           c
 *
           b
      +
           a
--------------------------------------------------
Infix : ((a+b)*(c*(d+e)))
Prefix : *+ab*c+de
```

Testcase #2
```
Enter Postfix : abc*+de*f+g*+
Tree :
           g
      *
                f
           +
                     e
                *
                     d
 +
                c
           *
                b
      +
           a
--------------------------------------------------
Infix : ((a+(b*c))+(((d*e)+f)*g))
Prefix : ++a*bc*+*defg
```

Testcase #3
```
Enter Postfix : ab+c*de-fg+*-
Tree :
                g
           +
                f
      *
                e
           -
                d
 -
           c
      *
                b
           +
                a
--------------------------------------------------
Infix : (((a+b)*c)-((d-e)*(f+g)))
Prefix : -*+abc*-de+fg
```

Testcase #4 - Hidden <br>
Testcase #5 - Hidden <br>
Testcase #6 - Hidden <br>