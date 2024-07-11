import random

def generate_bracket_string(length):
    brackets = ['(', ')', '{', '}', '[', ']']
    stack = []
    result = []

    while len(result) < length:
        if len(stack) == 0 or (len(stack) < (length - len(result)) // 2 and random.random() < 0.5):
            # Open a new bracket
            bracket = random.choice(['(', '{', '['])
            stack.append(bracket)
            result.append(bracket)
        else:
            # Close the last opened bracket
            bracket = stack.pop()
            if bracket == '(':
                result.append(')')
            elif bracket == '{':
                result.append('}')
            elif bracket == '[':
                result.append(']')

    # Close all remaining opened brackets
    while stack:
        bracket = stack.pop()
        if bracket == '(':
            result.append(')')
        elif bracket == '{':
            result.append('}')
        elif bracket == '[':
            result.append(']')

    return ''.join(result)


N = 20_000_000


# Generate the bracket string
bracket_string = generate_bracket_string(N)

# Save it to a text file
with open('bracket_string.txt', 'w') as file:
    file.write(bracket_string)