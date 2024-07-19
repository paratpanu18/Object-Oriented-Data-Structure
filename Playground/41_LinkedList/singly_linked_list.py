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
        return " -> ".join([str(i) for i in result])
    
    def __getitem__(self, index: int):
        return self.get_node_by_index(index)

    
data = SinglyLinkedList()
data.append(5)
data.append(10)
data.append(15)
data.append(20)
data.removeHead()
data.insertAfter(index= 1, data=30)
print(data[2])
        