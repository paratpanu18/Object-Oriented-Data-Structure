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

        if index >= self.size:
            return None

        current_node = self.head.next
        for _ in range(index):
            if current_node.next:
                current_node = current_node.next
        
        return current_node
    
    def isLooped(self):
        '''
            Floyd’s Cycle Finding Algorithm by ChatGPT kun
        '''
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def __str__(self):
        if self.isEmpty():
            return "Empty"

        result = []
        current = self.head.next    # Skip the header node
        while current:
            result.append(current.data)
            current = current.next
        return "->".join([str(i) for i in result])
    
    def __getitem__(self, index: int):
        return self.get_node_by_index(index)

class App:
    def __init__(self, commands):
        self.linked_list = SinglyLinkedList()
        self.commands = commands
    
    def run(self):
        commands_list = self.commands.split(',')
        for command in commands_list:
            self.validate_command(command)

        if self.linked_list.isLooped() :
            print('Found Loop') 
            exit()
            
        else:
            print('No Loop')
            print(self.linked_list)
            exit()

    def validate_command(self, command):
        signal = command[0]
        parameter = command[2:]

        if signal == 'A':
            self.linked_list.append(parameter)
            print(self.linked_list)

        elif signal == 'S':

            if self.linked_list.isEmpty():
                print('Error! {list is empty}')
                return

            index1, index2 = parameter.split(':')
            index1, index2 = int(index1), int(index2)
        
            node1 = self.linked_list.get_node_by_index(index1)
            if not node1:
                print('Error! {index not in length}:', index1)
                print('Loop Found') if self.linked_list.isLooped() else print('No Loop')
                print(self.linked_list)
                exit()

            node2 = self.linked_list.get_node_by_index(index2)
            if not node2:
                print(f'index not in length, append : {index2}')
                self.linked_list.append(index2)
            else:
                '''
                    [] -> [node1] -> [] -> [node2] -> []
                '''
                node1.next = node2
                print(f'Set node.next complete!, index:value = {index1}:{node1.data} -> {index2}:{node2.data}')

raw_commands = input("Enter input : ")
app = App(raw_commands)
app.run()