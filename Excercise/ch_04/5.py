class Queue:
    def __init__(self, lst: list = None) -> None:
        self.items: list = lst if lst else []
    
    def enQueue(self, new_item) -> None:
        self.items.append(new_item)
    
    def deQueue(self):
        return self.items.pop(0)
    
    def getQueue(self):
        return self.items
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def head(self):
        return self.items[0]
    
    def __getitem__(self, index):
        return self.items[index]

class Maze:

    DIRECTIONS = [(-1, 0), (0,1), (1,0), (0, -1)]

    def __init__(self, width, height, raw_map):
        self.size_x = width
        self.size_y = height

        if self.size_x <= 1 or self.size_y <= 1:
            raise ValueError("Invalid map input.")

        self.map = raw_map.split(",")

        print("\n".join(self.map))

        self.start_point = self.get_start_point()
        self.exit_point = self.get_exit_point()

        if not self.start_point or not self.exit_point \
            or len(self.map) != self.size_y \
            or any(len(row) != self.size_x for row in self.map):

            raise ValueError("Invalid map input.")

    def get_start_point(self):
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == "F":
                    return (x, y)
        return None
    
    def get_exit_point(self):
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == "O":
                    return (x, y)
        return None
                
    def can_move_to(self, x, y):
        return 0 <= x < self.size_x and 0 <= y < self.size_y

    def solve(self):
        ans = Queue()
        ans.enQueue(self.start_point)

        visited = set()
        visited.add(self.start_point)

        found_exit = False

        while not found_exit:
            if ans.isEmpty():
                print("Cannot find exit portal.")
                return

            print("Queue:", ans.getQueue())
            current_position = ans.deQueue()

            for dx, dy in self.DIRECTIONS:
                new_x, new_y = current_position[0] + dx, current_position[1] + dy

                if self.can_move_to(new_x, new_y):
                    if (new_x, new_y) not in visited:
                        if self.map[new_y][new_x] == "_":
                            ans.enQueue((new_x, new_y))
                            visited.add((new_x, new_y))
                        elif self.map[new_y][new_x] == "O":
                            print("Found the exit portal.")
                            return
        
        print("Cannot find exit portal.")
        return

inp = input("Enter width, height, and room: ").split()

size_x, size_y = int(inp[0]), int(inp[1])
raw_map = inp[2]

try:
    maze = Maze(size_x, size_y, raw_map)
    maze.solve()
except ValueError as e:
    print(e)
