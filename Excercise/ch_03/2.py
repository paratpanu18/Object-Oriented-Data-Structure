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
    class Dish:
        def __init__(self, weight: int, frequency: int):
            self.weight: int = weight
            self.frequency: int = frequency

    def __init__(self, command: list):
        self.commands_list: list = command
        self.stack = ArrayStack()
        self.answer = []
    
    def perform_operation(self, command: str):
        weight, frequency = [int(number) for number in command.split()]
        new_plate = self.Dish(weight, frequency)

        if self.stack.isEmpty() or new_plate.weight <= self.stack.top().weight:
            self.stack.push(new_plate)
            return 
        
        while not self.stack.isEmpty() and new_plate.weight >= self.stack.top().weight:
            self.answer.append(str(self.stack.pop().frequency))
        self.stack.push(new_plate)

    def start(self):
        for command in self.commands_list:
            self.perform_operation(command)
        
        return "\n".join(self.answer)

raw = [str(cmd) for cmd in input("Enter Input : ").split(',')]
app = App(raw)
print(app.start())