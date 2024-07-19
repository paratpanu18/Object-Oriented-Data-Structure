class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def __getitem__(self, i:int):
        return self.items[i]

class Maze:

    DIRECTIONS = [(-1, 0), (0,1), (1,0), (0, -1)]

    def __init__(self, size_x, size_y, raw_map):
        self.size_x: int = size_x
        self.size_y: int = size_y
        self.map: list = raw_map.split(",")

        if len(self.map) != self.size_y or \
            any(len(row) != self.size_x for row in self.map) or \
            not self.get_start_point():

            print("Invalid map input.")
            quit()


    def get_start_point(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.map[y][x] == "F":
                    return (x, y)
        return None
    
    def get_exit_point(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.map[y][x] == "O":
                    return (x, y)
        return None

    def solve(self):
        map = self.map
        direction = self.DIRECTIONS

        start = self.get_start_point()

        ans = Queue()
        ans.enQueue(start)

        visited = Queue()
        found = False

        while not found:
            if ans.isEmpty():
                print("Cannot reach the exit portal.")
                exit()
            else:
                print("Queue:",ans.items)
                axis = ans.deQueue()
                x1, y1 = axis[1], axis[0]
                for x2, y2 in direction:
                    (new_x, new_y) = (x1 + x2, y1 + y2)
                    if 0 <= new_x < self.size_y and 0 <= new_y < self.size_x:
                        if map[new_x][new_y] == "_"  and (new_y, new_x) not in visited:
                            ans.enQueue((new_y,new_x))
                            visited.enQueue((new_y, new_x))
                        elif map[new_x][new_y] == "O":
                            print("Found the exit portal.")
                            exit()


inp = input("Enter width, height, and room: ").split()
maze = Maze(size_x = int(inp[0]), 
            size_y = int(inp[1]), 
            raw_map = inp[2])

maze.solve()