class HashTable:
    def __init__(self, size: int, max_collision: int, threshold: float) -> None:
        self.size = 0
        self.max_size = size
        self.max_collision = max_collision
        self.threshold = threshold
        self.table = [None] * size
        self.data = []

    def __str__(self) -> str:
        data = []
        for i, value in enumerate(self.table, 1):
            data.append(f"#{i}\t{value}")
        
        return '\n'.join(data)

    def isFull(self) -> bool:
        return self.size == self.max_size
    
    def is_over_threshold(self) -> bool:
        return (self.size + 1) / self.max_size > self.threshold/100
    

    def rehash(self) -> None:
        # current_data = [int(data) for data in self.table if data is not None]
        current_data = self.data.copy()
        self.data.clear()
        
        self.max_size *= 2
        self.max_size += 1
        
        while not isPrime(self.max_size):
            self.max_size += 2
            
        self.table = [None] * self.max_size
        self.size = 0
        
        for data in current_data:
            self.hash(data)

    def hash_function(self, data: int) -> int:
        return int(data) % self.max_size
    
    def hash(self, data):
        collision = 0
        index = self.hash_function(data)
        current_index = index
        
        while self.table[index] and collision < self.max_collision:
            collision += 1
            print(f'collision number {collision} at {index}')
            index = (current_index + pow(collision, 2)) % self.max_size

        if collision >= self.max_collision:
            print('****** Max collision - Rehash !!! ******')
            self.rehash()
            hash_table.hash(data)
            return
        
        if self.is_over_threshold():
            print('****** Data over threshold - Rehash !!! ******')
            self.rehash()
            self.hash(data)
            return

        self.table[index] = data
        self.data.append(int(data))
        self.size += 1

def isPrime(data):
    i = 3
    if data % 2 == 0:
        return False
    while i <= data/2:
        if data % i == 0:
            return False
        i += 2
    return True
    

print(' ***** Rehashing *****')
inp = input('Enter Input : ').split('/')
size, max_collision, threshold = inp[0].split(' ')
hash_table = HashTable(int(size), int(max_collision), int(threshold))

print('Initial Table :')
print(hash_table)
print('----------------------------------------')

for i in inp[1].split(' '):
    print(f'Add : {i}')
    hash_table.hash(int(i))
    print(hash_table)
    print('----------------------------------------')