def infix_to_postfix(infix: str) -> str:
    PRIORITY = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    postfix = []
    stack = []

    for c in infix:
        if c.isalpha() or c == '(':
            postfix.append(c)
        
        elif c == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        
        else:
            while stack != [] and \
            stack[-1] != '(' and \
            PRIORITY[c] <= PRIORITY[stack[-1]]:
                postfix.append(stack.pop())
            
            stack.append(c)

    while stack != []:
        postfix.append(stack.pop())

    return "".join(postfix)

print(infix_to_postfix('a*b+c'))