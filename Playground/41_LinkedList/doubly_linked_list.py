class DoublyLinkedList:
    class Node:
        def __init__(self, data = None, prev = None, next = None):
            self.data = data
            self.prev = prev
            self.next = next
        
        def __str__(self):
            return str(self.data)
    
    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.tail.next = self.head
        self.head.next = self.tail
        self.size = 0

    def __str__(self):
        if self.isEmpty(): return "Empty"

        current_node = self.head.next
        datas = []
        while current_node != self.tail:
            datas.append(current_node.data)
            current_node = current_node.next
        
        return " -> ".join([str(data) for data in datas])
    
    def __getitem__(self, index: int):
        return self.get_node_by_index(index).data
    
    def __contains__(self, data) -> bool:
        current_node = self.head
        while current_node != self.tail:
            if current_node.data == data:
                return True
            current_node = current_node.next

        return False
    
    def isEmpty(self):
        return self.size == 0
    
    def get_node_by_index(self, index: int):
        if index < 0:
            index += self.size

        current_node = self.head.next
        for _ in range(index):
            current_node = current_node.next
        
        return current_node

    def append(self, data: any):
        current_node = self.head

        while current_node.next != self.tail:
            current_node = current_node.next

        '''
            [head] -> [] -> [] -> [current_node] -> [tail]
            [head] -> [] -> [] -> [current_node] -> {new_node} -> [tail]
        '''
        new_node = self.Node(data=data, prev=current_node, next=self.tail)
        self.tail.prev = new_node
        current_node.next = new_node

        self.size += 1

    def appendHead(self, data):
        '''
            [head] ->  [] -> [] -> [tail]
            [head] -> {new_node} -> [] -> [] -> [tail]
        '''

        current_first_node = self.head.next
        new_node = self.Node(data=data, prev=self.head, next=current_first_node)
        self.head.next = new_node
        current_first_node.prev = new_node

        self.size += 1
    
    def insert(self, data, index: int):
        '''
        [head] -> [prev_node] -> [next_node] -> [] -> [tail]
        [head] -> [prev_node] -> {inserted_node} -> [next_node] -> [] -> [tail]
        '''

        if index < 0:
            index += self.size

        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        prev_node = self.get_node_by_index(index)
        next_node = prev_node.next

        inserted_node = self.Node(data=data, prev=prev_node, next=next_node)
        prev_node.next = inserted_node
        next_node.prev = inserted_node

        self.size += 1

    def reversed(self):
        if self.isEmpty():
            return "Empty"
        
        current_node = self.tail
        reversed_list = []
        while current_node.prev is not self.head:
            reversed_list.append(str(current_node.prev.data))
            current_node = current_node.prev

        return reversed_list
    
    def remove(self, index: int = -1):
        '''
            [head] -> [] -> [] -> [last_node] -> [tail]
        '''
        
    def remove(self, index: int = -1):
        if self.isEmpty():
            raise IndexError("Remove from empty list")

        if index < 0:
            index += self.size

        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current_node = self.head.next
        for _ in range(index):
            current_node = current_node.next

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev

        self.size -= 1
        return current_node.data

data = DoublyLinkedList()
data.append(5)
data.append(10)
data.append(15)
data.append(20)
data.append(25)
data.remove(index=2)
print(data)