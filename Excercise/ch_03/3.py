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

def sign_piority(self, sign):
    if sign in '+-':
        return 1
    elif sign in '*/':
        return 2
    elif sign == '^':
        return 3

def isOperand(c):
    return c.isalpha()

def isLeftParenthesis(c):
    return c == '('

def isRightParenthesis(c):
    return c == ')'

def hasLessOrEqualPriority(x, y):
    precedence = {'+':1, '-':1, '*':2, '/':2, '%':2, '^':3}
    if y == '(':
        return False
    a = precedence[x]
    b = precedence[y] 
    if a  <= b:
        return True
    else:
        return False

def toPostfix(infix):
    stack = ArrayStack()
    postfix = ''

    for c in infix:
        if isOperand(c):
            postfix += c
        else:
            if isLeftParenthesis(c):
                stack.push(c)
            elif isRightParenthesis(c):
                operator = stack.pop()
                while not isLeftParenthesis(operator):
                    postfix += operator
                    operator = stack.pop()              
            else:
                while (not stack.isEmpty()) and hasLessOrEqualPriority(c,stack.top()):
                    postfix += stack.pop()
                stack.push(c)

    while (not stack.isEmpty()):
        postfix += stack.pop()
    return postfix

print(f'Postfix : {toPostfix(input("Enter Infix : "))}')