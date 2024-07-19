class SinglyLinkedList:
    class Node:
        def __init__(self, data = None):
            self.data = data
            self.next = None
        
        def __str__(self) -> str:
            return str(self.data)
    
    def __init__(self):
        self.head = self.Node()
        self.size = 0

    def get_last_node(self):
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        return last_node
    
    def append(self, data: any):
        new_node = self.Node(data)
        last_node = self.get_last_node()
        last_node.next = new_node
        self.size += 1

    def removeTail(self):
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        
        second_last_node = current_node
        del current_node

        p = second_last_node.next
        second_last_node.next = None

        self.size -= 1

        return p.data
    
    def removeHead(self):
        p = self.head.next.next
        self.head.next = p
        self.size -= 1

    def insertAfter(self, index: int, data: any):
        new_node = self.Node(data)
        current_node = self.head.next
        for _ in range(index):
            if current_node.next:
                current_node = current_node.next
                
        new_node.next = current_node.next
        current_node.next = new_node
        self.size += 1

    def removeAfter(self, index: int):
        current_node = self.head.next
        for _ in range(index - 1):
            if current_node.next:
                current_node = current_node.next
        
        p = current_node.next
        current_node.next = current_node.next.next
        self.size -= 1

        return p.data

    def isEmpty(self):
        return self.size == 0
    
    def get_node_by_index(self, index: int):
        if index < 0:
            index += self.size

        current_node = self.head.next
        for _ in range(index):
            current_node = current_node.next
        
        return current_node
    
    def __str__(self):
        result = []
        current = self.head.next    # Skip the header node
        while current:
            result.append(current.data)
            current = current.next
        return " <- ".join([str(i) for i in result])
    
    def __getitem__(self, index: int):
        return self.get_node_by_index(index).data

    
class LocoMotive:
    def __init__(self, seq: list) -> None:
        self.train = SinglyLinkedList()
        for car in seq:
            self.train.append(car)
    
    def re_arrange(self):
        '''
        [head] -> [first_node] -> [current_node] -> 0 -> [next_node] -> [] 
        [head] -> 0 -> [next_node] -> [] -> [first_node] -> []
        '''


        current_node = self.train.head.next
        if current_node.data == 0:
            return
        
        while current_node.next.data != 0:
            current_node = current_node.next
        
        zero_node = current_node.next
        last_node = self.train.get_last_node()
        first_node = self.train.head.next

        self.train.head.next = zero_node

        last_node.next = first_node
        current_node.next = None


    def __str__(self):
        return str(self.train)

print(" *** Locomotive ***")
raw_input = input("Enter Input : ").split()
train = LocoMotive([int(i) for i in raw_input])
print(f'Before : {train}')
train.re_arrange()
print(f'After : {train}')
        
        