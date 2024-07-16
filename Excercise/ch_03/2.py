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
        new_weight = int(command.split()[0])
        new_frequency = int(command.split()[1])
        new_plate = {"weight": new_weight,
                    "frequency": new_frequency}
        
        # print(new_plate)
        
        if self.stack.isEmpty():
            
            self.stack.push(new_plate)
        
        elif new_weight <= self.stack.top()["weight"]:
            self.stack.push(new_plate)
        
        else:
            # print(self.stack.data)
            while not self.stack.isEmpty() and new_weight >= self.stack.top()["weight"]:
                print(self.stack.pop()["frequency"])
            self.stack.push(new_plate)

    def start(self):
        for command in self.commands_list:
            self.perform_operation(command)

raw = [str(cmd) for cmd in input("Enter Input : ").split(',')]
app = App(raw)
app.start()