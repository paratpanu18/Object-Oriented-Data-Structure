class Queue:
    def __init__(self, lst: list = None) -> None:
        self.items: list = lst if lst else []
    
    def enQueue(self, new_item) -> None:
        self.items.append(new_item)
    
    def deQueue(self):
        return self.items.pop(0)
    
    def getQueue(self):
        return self.items
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
class App:
    def __init__(self, command: list):
        self.commands_list: list = command
        self.q = Queue()
    
    def perform_operation(self, command: str):
        signal = command[0]
        data = command[2::]

        if signal == 'E':
            self.q.enQueue(data)
            print(f'Add {data} index is {self.q.size() - 1}')
        
        if signal == 'D':
            if not self.q.isEmpty():
                print(f'Pop {self.q.deQueue()} size in queue is {self.q.size()}')
            else:
                print("-1")

    def start(self):
        for command in self.commands_list:
            self.perform_operation(command)

        if self.q.isEmpty():
            print("Empty")
        else:
            print(f'Number in Queue is :  {self.q.items}')
    
raw = [str(cmd) for cmd in input("Enter Input : ").split(',')]
app = App(raw)
app.start()

