import time

# Specify the file path
file_path = 'bracket_string.txt'

# Read the text from the file and store it in a string
with open(file_path, 'r') as file:
    text_string = file.read()

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
    
def is_valid_parentheses(data):
    S = ArrayStack()
    bracket_pairs = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    lefty_bracket = bracket_pairs.values()
    righty_bracket = bracket_pairs.keys()

    for c in data:
        '''
        Normal Character Case (Not match any bracket type)
        '''
        if (c not in lefty_bracket) and (c not in righty_bracket):
            continue

        if c in lefty_bracket:
            S.push(c)
        
        elif S.pop() != bracket_pairs[c]:
            return False
        
    return S.is_empty()


start = time.time()
print(is_valid_parentheses(text_string))
stop = time.time()
print ("%5.1f secs" % (stop - start))