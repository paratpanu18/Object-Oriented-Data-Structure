import time

# Specify the file path
file_path = 'bracket_string.txt'

# Read the text from the file and store it in a string
with open(file_path, 'r') as file:
    text_string = file.read()

def is_correct(data):
    pairs = {
        "}" : "{",
        ")" : "(",
        "]" : "["
    }

    temp = []

    for c in data:
        if c in pairs.values():
            temp.append(c)
        elif c in pairs.keys():
            key = pairs[c]

            if key not in temp:
                return False

            temp.remove(key)
            del c

    if len(temp) != 0:          # Temp is not empty
        return False
    
    return True

class ArrayStack:
    def __init__(self):
        self.data = []

    def push(self, obj):
        self.data.append(obj)

    def pop(self):
        return self.data.pop()
    
    def is_empty(self):
        return len(self.data) == 0
    
def is_correct_2(data):
    S = ArrayStack()
    lefty = '{(['
    righty = '})]'

    for c in data:
        if c in lefty:
            S.push(c)
            continue

        if righty.index(c) != lefty.index(S.pop()):
            return False
    
    del S
    return True

def is_valid_parentheses(s):
    stack = []
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_parentheses.values():
            stack.append(char)
        elif char in matching_parentheses.keys():
            if stack == [] or stack.pop() != matching_parentheses[char]:
                return False
        else:
            # If the character is not a parenthesis, you can either ignore it or return False
            # return False  # Uncomment this line if you want to return False for non-parentheses characters
            pass
    
    return stack == []



start = time.time()
# result = is_correct(text_string)
result = is_correct_2(text_string)
# result = is_valid_parentheses(text_string)
stop = time.time()
print ("%5.1f secs" % (stop - start))