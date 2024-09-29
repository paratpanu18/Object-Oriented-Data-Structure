class ArrayStack:
    def __init__(self):
        self.data = []

    def push(self, d):
        self.data.append(d)

    def pop(self) -> any:
        return self.data.pop()

    def top(self) -> any:
        return self.data[-1]
    
    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data) == 0

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        return str(self.val)
    
class ExpressionTree:
    def __init__(self, root = None):
        self.root = root if root else None
    
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return Node(key)
        if key in '+-*/':
            root.right = self._insert(root.right, key)
        else:
            root.left = self._insert(root.left, key)
        return root
    
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root:
            if root.val in '+-*/':
                print('(', end="")
            self._inorder(root.left)
            print(root.val, end="")
            self._inorder(root.right)
            if root.val in '+-*/':
                print(')', end="")

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, root):
        if root:
            print(root.val, end="")
            self._preorder(root.left)
            self._preorder(root.right)
    
    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.val, end="")
    
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
    
S = ArrayStack()
tree = ExpressionTree()
expression = '+-*/'
postfix = input('Enter Postfix : ')

for i in postfix:
    if i in expression:
        node = Node(i)
        node.right = S.pop()
        node.left = S.pop()
        S.push(node)
    else:
        S.push(Node(i))

tree.root = S.pop()
print("Tree :")
printTree90(tree.root)
print('--------------------------------------------------')
print(f'Infix : ', end="")
tree.inorder()
print(f'\nPrefix : ', end="")
tree.preorder()
