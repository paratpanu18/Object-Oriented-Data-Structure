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
        self.answer = []
    
    def perform_operation(self, command: str):
        if command.startswith('E'):
            _ , data = command.split()

            self.q.enQueue(data)
            self.answer.append(f'Add {data} index is {self.q.size() - 1}')
        
        if command.startswith('D'):
            self.answer.append(f'Pop {self.q.deQueue()} size in queue is {self.q.size()}' \
                               if not self.q.isEmpty() else "-1")

    def start(self):
        for command in self.commands_list:
            self.perform_operation(command)

        self.answer.append("Empty" if self.q.isEmpty() else f'Number in Queue is : {self.q.items}')
        
        return "\n".join(self.answer)
    
raw = [str(cmd) for cmd in input("Enter Input : ").split(',')]
app = App(raw)
print(app.start())

