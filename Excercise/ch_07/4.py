class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        return str(self.val)

class BST:
    def __init__(self, root = None):
        self.root = root if root else None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.val:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def inorder(self):
        self._inorder(self.root)
    
    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.val, end=" ")
            self._inorder(root.right)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, root):
        if root:
            print(root.val, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.val, end=" ")

    def bfs(self):
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

tree = BST()
input_data = [int(i) for i in input('Enter Input : ').split()]
for i in input_data:
    root = tree.insert(i)


print("Preorder : ", end="")
tree.preorder()

print("\nInorder : ", end="")
tree.inorder()

print("\nPostorder : ", end="")
tree.postorder()

print("\nBreadth : ", end="")
tree.bfs()

