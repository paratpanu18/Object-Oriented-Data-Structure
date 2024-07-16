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
    
    def perform_operation(self, command: str):
        signal = command[0]
        data = command[2::]

        if signal == 'A':
            self.stack.push(data)
            print(f'Add = {data} and Size = {self.stack.size()}')
        elif signal == 'P' and not self.stack.isEmpty():            
            popped_index = self.stack.size() - 1
            print(f'Pop = {self.stack.pop()} and Index = {popped_index}')
        
        else:
            print("-1")
            
    def start(self):
        for command in self.commands_list:
            self.perform_operation(command)

        if self.stack.isEmpty():
            print("Value in Stack = Empty")
            exit()

        remaining = "Value in Stack = "
        for value in self.stack.data:
            remaining += f'{value} '
        
        print(remaining)
        
    
raw = [str(cmd) for cmd in input("Enter Input : ").split(',')]
app = App(raw)
app.start()

