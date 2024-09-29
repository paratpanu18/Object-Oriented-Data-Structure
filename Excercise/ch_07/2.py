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
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    
    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp, arg = input('Enter Input : ').split('|')
inp = [int(i) for i in inp.split()]
arg = int(arg)

for i in inp:
    root = T.insert(i)
T.printTree(T.root)
result = []

def find_less(node, arg):
    if node is None:
        return
    find_less(node.left, arg)
    if node.data < arg:
        result.append(node.data)
    find_less(node.right, arg)

find_less(T.root, arg)


print('--------------------------------------------------')
if len(result) == 0:
    print(f'Below {arg} : Not have')
else:
    print(f'Below {arg} : {" ".join(map(str, result))}')