class Queue:
    def __init__(self, data = None) -> None:
        self.data = data if data else []
    
    def enQueue(self, new_item) -> None:
        self.data.append(new_item)

    def deQueue(self) -> any:
        return self.data.pop(0)
    
    def size(self) -> int:
        return len(self.data)
    
    def isEmpty(self) -> bool:
        return self.data == []
    
class SortingAlgorithm:
    def __init__(self, data = None):
        self.data = data if data else []
             
    def radix_sort(self) -> list:
        def get_digit(number, digit):
            return (number // (10 ** digit)) % 10
        
        digits = [Queue() for _ in range(10)]
        
        max_digit: int = len(str(max(self.data)))
        result = Queue(self.data)

        for digit in range(max_digit):
            while not result.isEmpty():
                num = result.deQueue()
                digits[get_digit(num, digit)].enQueue(num)
            
            for i in range(10):
                digit_queue: Queue = digits[i]
                while not digit_queue.isEmpty():
                    result.enQueue(digit_queue.deQueue())

        return result.data

nums = SortingAlgorithm([170, 45, 75, 90, 802, 24, 2, 66])
print(nums.radix_sort())