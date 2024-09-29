class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        # This will help you when debugging later.
        return f"Node({self.data})"

    def height(self):
        return (max(Node.height(self.left), Node.height(self.right)) + 1) if self else -1
    
    def balance(self):
        return Node.height(self.left) - Node.height(self.right) if self else 0

    def leftRotate(x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Return new root
        return y

    @staticmethod
    def rightRotate(y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Return new root
        return x

    def insert(root, data):
        # Step 1: Perform normal BST insert
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = Node.insert(root.left, data)
        else:
            root.right = Node.insert(root.right, data)

        # Step 2: Update balance factor and balance the tree
        balance = Node.balance(root)

        # Case 1 - Left Left (LL)
        if balance > 1 and data < root.left.data:
            return Node.rightRotate(root)

        # Case 2 - Right Right (RR)
        if balance < -1 and data > root.right.data:
            return Node.leftRotate(root)

        # Case 3 - Left Right (LR)
        if balance > 1 and data > root.left.data:
            root.left = Node.leftRotate(root.left)
            return Node.rightRotate(root)

        # Case 4 - Right Left (RL)
        if balance < -1 and data < root.right.data:
            root.right = Node.rightRotate(root.right)
            return Node.leftRotate(root)

        return root

    def find(self, data):
        if self is None:
            return None
        if self.data == data:
            return self
        if data < self.data:
            return Node.find(self.left, data)
        return Node.find(self.right, data)
    
    def find_parent(self, data):
        if self is None:
            return None
        if (self.left and self.left.data == data) or (self.right and self.right.data == data):
            return self
        if data < self.data and self.left:
            return self.left.find_parent(data)
        if data > self.data and self.right:
            return self.right.find_parent(data)
        return None

    def _gen_display(self) -> 'tuple[list, int, int, int]':
        '''
        return
        - tree image: list[str]
        - left spacing: int
        - value width: int
        - right spacing: int
        '''
        if self is None:
            return [], 0, 0, 0
        lt, lf, lv, lb = Node._gen_display(self.left)
        rt, rf, rv, rb = Node._gen_display(self.right)
        data = str(self.data)
        if not lt and not rt:
            return [data], 0, len(data), 0
        add_left, add_right = int(bool(lt)), int(bool(rt))
        line = ((' '*(lf+lv) + '/' + ' '*(lb)) * add_left +
                ' ' * len(data) +
                (' '*rf + '\\' + ' '*(rv+rb)) * add_right)
        out = [' '*(lf+lv+add_left) + '_'*lb + data +
               '_'*rf + ' '*(rv+rb+add_right), line]
        if len(lt) > len(rt):
            rt.extend([' ' * (rf+rv+rb)] * (len(lt) - len(rt)))
        elif len(lt) < len(rt):
            lt.extend([' ' * (lf+lv+lb)] * (len(rt) - len(lt)))
        for l, r in zip(lt, rt):
            out.append(l + ' '*(len(data)+add_left+add_right) + r)
        return out, (lf+lv+lb+add_left), len(data), (rf+rv+rb+add_right)


# rotate = node to be rotate
# direction = 'left' or 'right'
rotate, direction, inp = input('Enter input: ').split(',')
rotate = int(rotate)
root: Node | None = None
for i in map(int, inp.split()):
    root = Node.insert(root, i)
tree_image = root._gen_display()
print("Before")
print(*tree_image[0], sep='\n')
print("-" * sum(tree_image[1:]))

# Straighten a specified node with specified direction
# Generate new display: tree_image = Node._gen_display(<Node object at 0x80085>)
target_node = root.find(rotate)
parent_node = root.find_parent(rotate)

print("After")
tree_image = target_node._gen_display()
print(*tree_image[0], sep='\n')