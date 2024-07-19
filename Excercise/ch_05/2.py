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
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    
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
    
    def get_node_by_data(self, data):
        current_node = self.head.next
        while current_node != self.tail:
            if current_node.data == data:
                return current_node
            current_node = current_node.next

        return None

class App:
    def __init__(self, commands):
        self.commands = commands
        self.linked_list = DoublyLinkedList()

    def run(self):
        for command in self.commands:
            command, parameter = command.split()
            self.validate_commands(command, parameter)

    def validate_commands(self, command, parameter):
        if command == "AP":
            self.linked_list.append(parameter)
        elif command == "AH":
            self.linked_list.appendHead(parameter)
        elif command == "SE":
            if parameter in self.linked_list:
                print(f"Found {parameter} in {self.linked_list}")
            else:
                print(f"Not found {parameter} in {self.linked_list}")
        elif command == "SI":
            print(f"Linked List size = {self.linked_list.size} : {self.linked_list}")
        elif command == "ID":
            print(f"Index ({parameter}) = {self.linked_list.get_node_by_data(parameter).data} : {self.linked_list}")
        elif command == "PO":
            before = str(self.linked_list)
            k = self.linked_list.remove(parameter)
            
        elif command == "IS":
            data = parameter.split()
            self.linked_list.insert(data=data[1], index=int(data[0]))


raw_input = input("Enter input : ").split(",")
