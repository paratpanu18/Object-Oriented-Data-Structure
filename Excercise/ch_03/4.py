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
    
    def clear(self):
        self.data = []

class App:
    def __init__(self, command: list):
        self.commands_list: list = command
        self.stack = ArrayStack()
    
    def perform_operation(self, command: str):
        signal = command[0]
        height = command[2::]

        if signal == 'A':
            self.stack.push(height)
        
        if signal == 'B':
            visible_tree = []
            current_stack: list = self.stack.data.copy()
            lst_len = len(current_stack)

            for _ in range(lst_len):
                nearest_tree = current_stack.pop()
                # print(f'Nearest: {nearest_tree} / Visible {visible_tree} / Current {current_stack}')
                if not visible_tree: 
                    visible_tree.append(int(nearest_tree))

                elif int(nearest_tree) > int(visible_tree[-1]):
                    visible_tree.append(int(nearest_tree))

                elif int(nearest_tree) < int(visible_tree[-1]):
                    continue
            
            print(len(visible_tree))
            
    def start(self):
        for command in self.commands_list:
            self.perform_operation(command)
        
    
raw = [str(cmd) for cmd in input("Enter Input : ").split(',')]
app = App(raw)
app.start()

