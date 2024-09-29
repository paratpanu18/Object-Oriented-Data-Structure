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
    
    def bf(self):
        return Node.height(self.left) - Node.height(self.right) if self else 0

    def leftRotate(z):
        # Left rotate
        
        y = z.right 
        z.right = y.left
        y.left = z
        
        return y
        

    def rightRotate(z):
        # Right rotate
        
        y = z.left
        z.left = y.right
        y.right = z
        
        return y
    
    def add(root, data, direction):
        if root is None:
            return Node(data)
        
        if direction == 'left':
            branch = "left"
        elif direction == 'right':
            branch = "right"
            
        root.__dict__[branch] = Node.add(root.__dict__[branch], data, direction)
        return root
    
    
    def insert(root, data):
        if root is None:
            return Node(data)
        branch = "left" if data < root.data else "right"
        root.__dict__[branch] = Node.insert(root.__dict__[branch], data)

        # Balance this tree
        if root.bf() > 1 and root.left.bf() > 0:
            return Node.rightRotate(root)
        
        if root.bf() < -1 and root.right.bf() < 0:
            return Node.leftRotate(root)
        
        if root.bf() > 1 and root.left.bf() < 0:
            root.left = Node.leftRotate(root.left)
            return Node.rightRotate(root)
        
        if root.bf() < -1 and root.right.bf() > 0:
            root.right = Node.rightRotate(root.right)
            return Node.leftRotate(root)
        
        return root

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

    def to_bad_tree(self, direction, target): #target to rotate 
        
        default_root = self
        
        def find_root_of_target(root, target):
            #return root of the target
                
            if root is None:
                return None
            
            if root.left is None and root.right is None and root.data != target:
                print(f"No {target} in this tree")
                exit()
                
            if root.data == target:
                return root
            if target > root.data:
                return find_root_of_target(root.right, target)
            if target < root.data:
                return find_root_of_target(root.left, target)   
            
        def get_list_of_node(root):
            if root is None:
                return []
            return [root.data] + get_list_of_node(root.left) + get_list_of_node(root.right)
        
        def link_2_root_on_target(default_root,new_root, target):
            if default_root is None:
                return None
            if default_root.data == target:
                return new_root
            if target > default_root.data:
                default_root.right = link_2_root_on_target(default_root.right, new_root, target)
            if target < default_root.data:
                default_root.left = link_2_root_on_target(default_root.left, new_root, target)
                
            return default_root
        
        
        root = find_root_of_target(self, target)
        new_root = None 
        
        if direction == 'left':
            list_of_node = get_list_of_node(root)
            list_of_node.sort(reverse=True)

        elif direction == 'right': # default method sort 
            list_of_node = get_list_of_node(root)
            list_of_node.sort()
            
        for i in list_of_node:
            new_root = Node.add(new_root, i, direction)
  
        new_tree = link_2_root_on_target(default_root, new_root, target)
        
        tree = new_tree._gen_display()
        print("After")
        print(*tree[0], sep='\n')

        return new_tree     
        
rotate, direction, inp = input('Enter input: ').split(',')
rotate = int(rotate)
root = None
for i in map(int, inp.split()):
    root = Node.insert(root, int(i))
tree_image = root._gen_display()
print("Before")
print(*tree_image[0], sep='\n')
print("-" * sum(tree_image[1:]))

# Straighten a specified node with specified direction
# Generate new display: tree_image = Node._gen_display(<Node object at 0x80085>)

root.to_bad_tree(direction, rotate)