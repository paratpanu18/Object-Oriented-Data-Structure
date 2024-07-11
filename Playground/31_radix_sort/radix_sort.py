from collections import deque

class Queue:
    def __init__(self, initial_items: list = None):
        self.items: deque = deque(initial_items) if initial_items else deque()

    def enQueue(self, new_item):
        self.items.append(new_item)
    
    def deQueue(self):
        return self.items.popleft()
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.size() == 0
    
class RedixSort:
    @staticmethod
    def get_digit(number, digit):
        for i in range(digit - 1):
            number //= 10

        return number % 10
    
    @staticmethod
    def radix_sort(self):
        pass

[1,2,3,4].radix_sort()