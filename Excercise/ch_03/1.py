class ArrayStack:
    def __init__(self):
        self.data = []

    def push(self, d):
        self.data.append(d)

    def pop(self) -> any:
        return self.data.pop()

    def top(self) -> any:
        return self.data[-1]
    
    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data) == 0

class App:
    def __init__(self, command: list):
        self.commands_list: list = command
        self.stack = ArrayStack()
        self.answer = []
    
    def perform_operation(self, command: str):
        if command.startswith('A'):
            _ , data = command.split()
            self.stack.push(data)
            self.answer.append(f'Add = {data} and Size = {self.stack.size()}')

        elif command.startswith('P') and not self.stack.isEmpty():            
            self.answer.append(f'Pop = {self.stack.pop()} and Index = {self.stack.size()}')
        
        else:
            self.answer.append("-1")
            
    def start(self):
        for command in self.commands_list:
            self.perform_operation(command)

        if self.stack.isEmpty():
            self.answer.append("Value in Stack = Empty")
            return "\n".join(self.answer)

        remaining = "Value in Stack = "
        for value in self.stack.data:
            remaining += f'{value} '
        
        self.answer.append(remaining)
        return "\n".join(self.answer)
        
    
raw = [str(cmd) for cmd in input("Enter Input : ").split(',')]
app = App(raw)
print(app.start())

