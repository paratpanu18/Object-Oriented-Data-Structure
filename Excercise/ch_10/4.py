class HashTable:
    def __init__(self, size, max_collision, threshold):
        self.size = size
        self.table = [None] * size
        self.max_collision = max_collision
        self.threshold = threshold
        self.count = 0 

    def hash_function(self, key):
        return key % self.size

    def find_next_prime(self, n):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        prime = n
        while not is_prime(prime):
            prime += 1
        return prime

    def rehash(self):
        old_table = self.table
        new_size = self.find_next_prime(self.size * 2)
        print("****** Data over threshold - Rehash !!! ******")
        self.size = new_size
        self.table = [None] * new_size
        self.count = 0

        # Reinsert all elements from the old table into the new one
        for item in old_table:
            if item is not None:
                self.add(item, rehashing=True)

        self.display()  # Display the table after rehashing

    def add(self, key, rehashing=False):
        # Check if adding this key would exceed the threshold
        if (self.count + 1) * 100 / self.size >= self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()

        index = self.hash_function(key)
        collision_count = 0
        i = 1

        # Quadratic probing for collision resolution
        while self.table[index] is not None:
            if not rehashing:
                print(f"collision number {collision_count + 1} at {index}")
            collision_count += 1
            if collision_count >= self.max_collision:
                print("****** Max collision - Rehash !!! ******")
                self.rehash()
                return self.add(key)  # Re-attempt to add the key after rehashing

            index = (self.hash_function(key) + i ** 2) % self.size
            i += 1

        self.table[index] = key
        self.count += 1
        if not rehashing:
            print(f"Add : {key}")
            self.display()

    def display(self):
        for i, val in enumerate(self.table):
            print(f"#{i+1}\t{val}")
        print("----------------------------------------")

# Example usage
if __name__ == "__main__":
    # Input format: "size max_collision threshold / data"
    user_input = input("Enter Input: ").split('/')
    
    # Left part: size, max_collision, threshold
    left = list(map(int, user_input[0].split()))
    size, max_collision, threshold = left

    # Right part: data values
    data = list(map(int, user_input[1].split()))

    # Create HashTable object
    hash_table = HashTable(size, max_collision, threshold)
    
    print("Initial Table:")
    hash_table.display()

    # Insert each data value into the hash table
    for num in data:
        hash_table.add(num)
