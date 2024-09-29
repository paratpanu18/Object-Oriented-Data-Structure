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

class CashierQueue(Queue):
    def __init__(self, process_time: int, max_queue: int, lst: list = None) -> None:
        super().__init__(lst)
        self.process_time = process_time
        self.max_queue = max_queue
        self.timer = 0
    
    def tick(self):
        if not self.isEmpty():
            self.timer += 1
            if self.timer >= self.process_time:
                self.deQueue()
                self.timer = 0

    def isFulled(self):
        return self.size() >= self.max_queue

class QueueManager:
    def __init__(self, str: str, time: int):
        self.main_queue: Queue = Queue([c for c in str])
        self.cashier1_queue: CashierQueue = CashierQueue(process_time=3, max_queue=5)
        self.cashier2_queue: CashierQueue = CashierQueue(process_time=2, max_queue=5)
        self.time: int = time

    def run(self):
        for i in range(self.time):
            self.cashier1_queue.tick()
            self.cashier2_queue.tick()

            if not self.main_queue.isEmpty():
                if not self.cashier1_queue.isFulled():
                    self.cashier1_queue.enQueue(self.main_queue.deQueue())
                elif not self.cashier2_queue.isFulled():
                    self.cashier2_queue.enQueue(self.main_queue.deQueue())
        
            print(f"{i + 1} {self.main_queue.getQueue()} {self.cashier1_queue.getQueue()} {self.cashier2_queue.getQueue()}")

str_input, time_input = input("Enter people and time : ").split()
app = QueueManager(str_input, int(time_input))
app.run()
