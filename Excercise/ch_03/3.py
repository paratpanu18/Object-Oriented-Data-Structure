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

class InfixToPostfixConvertor:

    SIGN_PRIORITY = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    def __init__(self, infix: str) -> None:
        self.infix: str = infix
        self.stack: ArrayStack = ArrayStack()
        self.postfix: list = []

    def run(self):
        return self.convert_to_postfix()
    
    def convert_to_postfix(self) -> str:
        infix = self.infix
        for c in infix:
            if c.isalpha():
                self.postfix.append(c)
            
            elif c == '(':
                self.stack.push(c)

            elif c == ')':
                while not self.stack.isEmpty() and self.stack.top() != '(':
                    self.postfix.append(self.stack.pop())
                self.stack.pop()        # Pop '('
            
            else:
                while not self.stack.isEmpty() and \
                    self.stack.top() != '(' and \
                    InfixToPostfixConvertor.SIGN_PRIORITY[c] <= InfixToPostfixConvertor.SIGN_PRIORITY[self.stack.top()]:

                    self.postfix.append(self.stack.pop())
                self.stack.push(c)
                
        while not self.stack.isEmpty():
            self.postfix.append(self.stack.pop())
        
        return "".join(self.postfix)

app = InfixToPostfixConvertor(input())
print(app.run())