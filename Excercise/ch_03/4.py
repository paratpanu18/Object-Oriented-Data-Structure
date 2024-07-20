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
    def __init__(self, commands_list: list) -> None:
        self.tree_stack: ArrayStack = ArrayStack()
        self.commands_list: list = commands_list
        self.answer: list = []

    def start(self) -> str:
        for command in self.commands_list:
            self.perform_operation(command)
        return "\n".join(self.answer)
    
    def perform_operation(self, command: str):
        if command.startswith('A'):
            height = int(command.split()[1])

            while not self.tree_stack.isEmpty() and height >= self.tree_stack.top():
                self.tree_stack.pop()

            self.tree_stack.push(height)
            
        elif command.startswith('B'):
            self.answer.append(str(self.tree_stack.size()))

raw = [str(cmd) for cmd in input("Enter Input : ").split(',')]
app = App(raw)
print(app.start())