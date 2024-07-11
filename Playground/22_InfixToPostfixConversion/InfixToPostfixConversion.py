class ArrayStack:
    def __init__(self):
        self.data = []

    def push(self, obj):
        self.data.append(obj)

    def pop(self):
        return self.data.pop() if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)
    
    def peak(self):
        return self.data[-1]



def infix_to_postfix_convert(infix: str) -> str:
    '''
        Basic Infix to Postfix conversion - Without parentheses
    '''
    operator_stack = ArrayStack()

    operator = '+-*/'

    result = ''


    for c in infix:

        if c not in operator:         # If it is not an operator, then it have to be an operand
            result += c
        
        else:
            if operator_stack.is_empty():
                operator_stack.push(c)


    return result

print(infix_to_postfix_convert('a*b+c'))
