class AVLTree:
    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self) -> int:
                left_height: int = self.getHeight(self.left)
                right_height: int = self.getHeight(self.right)

                self.height: int = 1 + max(left_height, right_height)
                return self.height

        def getHeight(self, node):
            return -1 if node == None else node.height

        def balanceValue(self):      
            return self.getHeight(self.right) - self.getHeight(self.left)


    def __init__(self, root = None):
        self.root = None if root is None else root

    def add(self, data):
        self.root = AVLTree._add(self.root, data)

    def _add(root, data):
        if not root:
            return AVLTree.AVLNode(data)
        elif data < root.data:
            root.left = AVLTree._add(root.left, data)
        elif data > root.data:
            root.right = AVLTree._add(root.right, data)
        
        return AVLTree._balance(root)
    
    def rotateLeftChild(root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        root.setHeight()
        new_root.setHeight()
        
        return new_root
    
    def rotateRightChild(root) :
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        root.setHeight()
        new_root.setHeight()

        return new_root

    def postOrder(self):
        print("AVLTree post-order : ", end = '')
        AVLTree._postOrder(self.root)
        print()

    def _postOrder(root):
        if root is not None:
            AVLTree._postOrder(root.left)
            AVLTree._postOrder(root.right)
            print(root.data, end = ' ')

    def _balance(root):
        balance = root.balanceValue()

        # Right heavy case (balance > 1)
        if balance > 1:
            print("Not Balance, Rebalance!")
            if root.right.balanceValue() < 0:  # Right-Left case
                root.right = AVLTree.rotateRightChild(root.right)
            root = AVLTree.rotateLeftChild(root)
        
        # Left heavy case (balance < -1)
        elif balance < -1:
            print("Not Balance, Rebalance!")
            if root.left.balanceValue() > 0:  # Left-Right case
                root.left = AVLTree.rotateLeftChild(root.left)
            root = AVLTree.rotateRightChild(root)

        # Always update the height after rebalancing
        root.setHeight()
        return root



    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node , level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVLTree() 

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.add(int(e))
    printTree90(myTree.root)
    print("===============")