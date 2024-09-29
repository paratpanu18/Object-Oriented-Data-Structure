class DoublyLinkedList:
    class Node:
        def __init__(self, data = None, prev = None, next = None):
            self.data = data
            self.prev = prev
            self.next = next
        
        def __str__(self):
            return str(self.data)
    
    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.tail.next = self.head
        self.head.next = self.tail
        self.size = 0

    def __str__(self):
        if self.isEmpty(): return "Empty"

        current_node = self.head.next
        datas = []
        while current_node != self.tail:
            datas.append(current_node.data)
            current_node = current_node.next
        
        return " -> ".join([str(data) for data in datas])
    
    def __getitem__(self, index: int):
        return self.get_node_by_index(index).data
    
    def __contains__(self, data) -> bool:
        current_node = self.head
        while current_node != self.tail:
            if current_node.data == data:
                return True
            current_node = current_node.next

        return False
    
    def isEmpty(self):
        return self.size == 0
    
    def get_node_by_index(self, index: int):
        if index < 0:
            index += self.size

        current_node = self.head.next
        for _ in range(index):
            current_node = current_node.next
        
        return current_node

    def append(self, data: any):
        current_node = self.head

        while current_node.next != self.tail:
            current_node = current_node.next

        '''
            [head] -> [] -> [] -> [current_node] -> [tail]
            [head] -> [] -> [] -> [current_node] -> {new_node} -> [tail]
        '''
        new_node = self.Node(data=data, prev=current_node, next=self.tail)
        self.tail.prev = new_node
        current_node.next = new_node

        self.size += 1

    def appendHead(self, data):
        '''
            [head] ->  [] -> [] -> [tail]
            [head] -> {new_node} -> [] -> [] -> [tail]
        '''

        current_first_node = self.head.next
        new_node = self.Node(data=data, prev=self.head, next=current_first_node)
        self.head.next = new_node
        current_first_node.prev = new_node

        self.size += 1
    
    def insert(self, data, index: int):
        '''
        [head] -> [prev_node] -> [next_node] -> [] -> [tail]
        [head] -> [prev_node] -> {inserted_node} -> [next_node] -> [] -> [tail]
        '''

        if index < 0:
            index += self.size

        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        prev_node = self.get_node_by_index(index)
        next_node = prev_node.next

        inserted_node = self.Node(data=data, prev=prev_node, next=next_node)
        prev_node.next = inserted_node
        next_node.prev = inserted_node

        self.size += 1

    def reversed(self):
        if self.isEmpty():
            return "Empty"
        
        current_node = self.tail
        reversed_list = []
        while current_node.prev is not self.head:
            reversed_list.append(str(current_node.prev.data))
            current_node = current_node.prev

        return reversed_list

    def remove(self, index: int = -1):
        if self.isEmpty():
            raise IndexError("Remove from empty list")

        if index < 0:
            index += self.size

        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current_node = self.head.next
        for _ in range(index):
            current_node = current_node.next

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev

        self.size -= 1
        return current_node.data
    
class Snake(DoublyLinkedList):
    def __init__(self) -> None:
        super().__init__()
        pass

    def __str__(self):
        if self.size == 1:
            return f'({self.head.next.data})->Empty'

        second_to_last_snake = []

        current: self.Node = self.get_node_by_index(1)
        while current.next != self.tail:
            second_to_last_snake.append(str(current.data))
            current = current.next

        second_to_last_snake.append(str(current.data))

        return f'({self.get_node_by_index(0)})->' +  "->".join((second_to_last_snake))
    
    def sum(self) -> int:
        sum = 0

        current = self.head.next
        while current.next != self.tail:
            sum += int(current.data)
            current = current.next
        
        sum += int(current.data)
        
        return sum
    
    def swap_first_and_last(self):
        if self.head.next == self.tail or self.head.next.next == self.tail:
            return  # No need to swap if the list is empty or has only one node

        first = self.head.next
        last = self.tail.prev

        first_next = first.next
        last_prev = last.prev

        first.next = self.tail
        first.prev = last_prev
        last.prev = self.head
        last.next = first_next

        first_next.prev = last
        if last_prev:
            last_prev.next = first

        self.head.next = last
        self.tail.prev = first

    def can_eat(self, father_size: int) -> bool:
        data = []

        current = self.head.next.next
        while current != self.tail:
            data.append(int(current.data))
            current = current.next

        for i in data:
            if i == 0:
                continue

            elif father_size == 0 and i != 0:
                return True
            
            elif father_size % i == 0:
                return True
            
        return False
    
    def eat(self, father_size: int) -> list:
        eaten_snake: list = []
        total: int = self.sum()

        # print(f'Total: {total} Father: {father_size}')

        if total >= father_size:
            return eaten_snake

        if not self.can_eat(father_size):
            '''
            [head] -> [first] -> [] -> [] -> [] -> [] -> [last] -> [tail]
            [head] -> [last] -> [] -> [] -> [] -> [] -> [first] -> [tail]
            '''
            self.swap_first_and_last()
            return eaten_snake
        
        mother_node = self.head.next
        current_node = self.tail.prev

        while current_node.prev != mother_node:
            if current_node.data == 0 and father_size != 0:
                current_node = current_node.prev
                continue
            
            if father_size == 0 and current_node.data == 0:
                eaten_snake.append(current_node.data)
                self.remove()

            elif current_node.data != 0 and not father_size % current_node.data == 0:
                '''
                    [head] -> [mother] -> [] -> [current] -> [] -> [] -> [tail]
                '''
                eaten_snake.append(current_node.data)
                self.remove()

            else:
                return eaten_snake
            
            current_node = current_node.prev

        if father_size == 0 and current_node.data == 0:
                eaten_snake.append(current_node.data)
                self.remove()

        elif current_node.data != 0 and not father_size % current_node.data == 0:
            '''
                [head] -> [mother] -> [] -> [current] -> [] -> [] -> [tail]
            '''
            eaten_snake.append(current_node.data)
            self.remove()

        return eaten_snake
    
    def shake(self) -> list:
        '''
            [mother_node] -> [] -> [] -> [current] -> [] -> [] -> [tail]
        '''

        mother_node: self.Node = self.head.next
        mother_size: int = int(mother_node.data)
        current: self.Node = mother_node.next
        shook_snake = []

        while current != self.tail:
            current_size = int(current.data)
            if current_size > mother_size:
                shook_snake.append(int(current.data))

                current.prev.next = current.next
                current.next.prev = current.prev

                self.size -= 1

            current = current.next

        return shook_snake
    
    def swap(self):
        '''
            [head] -> [mother] -> [first] -> [second] -> [] -> [] -> [tail]
            [head] -> [mother] -> [second] -> [first] -> [] -> [] -> [tail]

        '''

        mother_node = self.head.next
        current_node = mother_node.next

        while current_node != self.tail and current_node.next != self.tail:
            first = current_node
            second = current_node.next

            first.next = second.next
            if second.next:
                second.next.prev = first

            second.prev = first.prev
            if first.prev:
                first.prev.next = second
            else:
                self.head = second

            second.next = first
            first.prev = second

            current_node = first.next

        if current_node.next == self.tail:
            current_node.prev.next = self.tail
            self.tail.prev = current_node.prev

            self.size -= 1
            
class SnakeGame:
    def __init__(self, initial_snake: list, commands_list: list) -> None:
        self.snake_linked_list = Snake()

        for snake in initial_snake:
            self.snake_linked_list.append(int(snake))

        self.commands_list = commands_list
        self.answer = []

        print(self.snake_linked_list)

    def run(self) -> str:
        for command in self.commands_list:
            
            self.validate_command(command)
            print(self.snake_linked_list)
            print('-' * 30)

            if self.snake_linked_list.size == 1:
                print('Mom is dead')
                break

        return "\n".join(self.answer)
    
    def validate_command(self, command: str) -> None:
        if command.startswith('SW'):
            '''
                Swap
            '''
            print('Swap success!')
            self.snake_linked_list.swap()
            pass

        elif command.startswith('SH'):
            '''
                Shake: Babies which its size greater than its mother will be popped out
            '''

            shook_snake = self.snake_linked_list.shake()
            print(f'Shake success!->{shook_snake}')

        elif command.startswith('F'):
            '''
                Steal: Append new snake to linked list
            '''

            _ , new_snake = command.split()

            self.snake_linked_list.append(int(new_snake))
            print(f'Steal success!->{new_snake}')

            pass

        elif command.startswith('D'):
            '''
                Eat
            '''

            _ , father_size = command.split()
            father_size = int(father_size)

            eaten_snake = self.snake_linked_list.eat(father_size)

            if eaten_snake:
                eaten_snake = list(reversed(eaten_snake))
            print(f'Play success!->{eaten_snake}')


initial_snake, commands = input('Snake Game : ').split('/')

initial_snake = initial_snake.split()
commands = commands.split(',')

app = SnakeGame(initial_snake, commands)
app.run()
print('Snake Game : ')