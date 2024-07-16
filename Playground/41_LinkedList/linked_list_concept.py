class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        self.size += 1

    def addHead(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def removeHead(self):
        p: Node = 0
        if self.head is None: 
            return None
        
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def __str__(self) -> str:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return "-> ".join([str(i) for i in result])

    def __getitem__(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    
data = LinkedList()
data.append(1)
data.append(2)
data.append(3)
data.removeHead()
data.addHead(0)
print(data)

