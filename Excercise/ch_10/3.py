class HashTable:
    class Data:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

        def __str__(self):
            return "({0}, {1})".format(self.key, self.value)

    def __init__(self, capacity, max_collision):
        self.size: int = 0
        self.capacity: int = capacity
        self.max_collision: int = max_collision
        self.table: list = [None] * capacity

    def __str__(self) -> str:
        result = ""
        for i in range(self.capacity):
            result += f"#{i + 1}	{self.table[i]}\n"

        result += '---------------------------'
        return result

    def hash_function(self, data: str) -> int:
        return sum([ord(c) for c in data]) % self.capacity
    
    def insert(self, key: str, value: str):
        index = self.hash_function(key)
        original_index = index
        collision_count = 0

        while collision_count < self.max_collision:
            if not self.table[index]:
                self.table[index] = HashTable.Data(key, value)
                self.size += 1
                print(self)
                return
            else:
                collision_count += 1
                print(f'collision number {collision_count} at {index}')
                index = (original_index + collision_count ** 2) % self.capacity

        print("Max of collisionChain")
        print(self)

    def is_full(self) -> bool:
        return self.size == self.capacity

print(' ***** Fun with hashing *****')
table_config, datas = input("Enter Input : ").split('/')
capacity, max_collision = [int(i) for i in table_config.split()]

table = HashTable(capacity, max_collision)

for data in datas.split(','):
    key, value = data.split()
    if table.is_full():
        print("This table is full !!!!!!")
        break
    table.insert(key, value)
