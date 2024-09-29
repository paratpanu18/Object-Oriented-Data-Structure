class Stack:
    def __init__(self, items = None) -> None:
        self.items: list = items if items else []
    
    def push (self, item) -> None:
        self.items.append(item)

    def pop(self) -> any:
        return self.items.pop()
    
    def isEmpty(self) -> bool:
        return self.items == []
    
    def size(self) -> int:
        return len(self.items)
    
    def __str__(self):
        return "".join([str(item) for item in self.items]) if not self.isEmpty() else "Empty"

class Queue:
    def __init__(self, items = None) -> None:
        self.items: list = items if items else []
    
    def enQueue(self, item):
        self.items.append(item)

    def deQueue(self) -> any:
        return self.items.pop(0)
    
    def isEmpty(self) -> bool:
        return self.items == []
    
    def size(self) -> int:
        return len(self.items)

class ColorCrush:

    EXPLOSIVE_STRIKE = 3

    def __init__(self, normal: str, mirror: str) -> None:
        self.answer: list = []
        self.normal: str = normal.upper()
        self.mirror: str = mirror.upper()
        pass

    def play(self) -> str:
        '''
            Mirror World will explode first
        '''

        mirror_remaining, mirror_exploded_letter = self.explosion_check(self.mirror)


        return "\n".join(self.answer)

    def explosion_check(self, pattern: str) -> tuple:
        exploded_letter = Queue()

        def explode(s):
            n = ColorCrush.EXPLOSIVE_STRIKE
            result = []
            i = 0

            while i < len(s):
                # Check if we have enough characters left for an explosion
                if i <= len(s) - n and s[i:i + n] == s[i] * n:
                    exploded_letter.enQueue(s[i])
                    i += n  # Skip over the exploded letters
                else:
                    result.append(s[i])
                    i += 1
            return ''.join(result)

        previous_length = -1
        while len(pattern) != previous_length:
            previous_length = len(pattern)
            pattern = explode(pattern)
            
        return (pattern, exploded_letter)


# normal, mirror = input("Enter Input (Normal, Mirror) :").split()
# game = ColorCrush(normal, mirror)
# print(game.play())
game = ColorCrush("","")
print(game.explosion_check("AABBBABC"))