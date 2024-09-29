class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new = Node(data)

        p = self.head
        if self.head == None:
            self.head = new
            self.tail = new
        else:
            while(p.next != None):
                p = p.next
            p.next = new
            new.previous = p
            self.tail = new
    
    def sw(self):
        swap_snake_list = []

        p = self.head.next
        if(p == None):
            return
        while(p != None):
            swap_snake_list.append(p.data)
            p = p.next

        if(len(swap_snake_list) % 2 == 1):
            swap_snake_list.append(None)

        for i in range(len(swap_snake_list)):
            if(i % 2 == 1):
                continue
            if(swap_snake_list[i+1] == None):
                swap_snake_list.pop()
                swap_snake_list.pop()
            else:
                temp = swap_snake_list[i]
                swap_snake_list[i] = swap_snake_list[i+1]
                swap_snake_list[i+1] = temp

        self.head.next = None
        self.tail = self.head
        
        for snake in swap_snake_list:
            self.append(snake)

        print("Swap success!")
        self.__str__()
        print("------------------------------")

    def sh(self):
        out_snakes = []

        p = self.head.next
        if(p == None):
            return
        while(p != None):
            if(p.data > self.head.data):
                if(p.next == None):
                    self.tail = p.previous
                    p.previous.next = None
                else:
                    p.previous.next = p.next
                    p.next.previous = p.previous
                out_snakes.append(p.data)
            p = p.next

        print(f"Shake success!->{out_snakes}")
        self.__str__()
        print("------------------------------")

    def f(self, data):
        p = self.head.next
        if(p == None):
            return
        
        self.append(data)

        print(f"Steal success!->{data}")
        self.__str__()
        print("------------------------------")

    def d(self, father_weight):
        total_weight = 0
        lost_snakes = []

        p = self.head
        while(p != None):
            total_weight += p.data
            p = p.next
        
        if(total_weight < father_weight):
            p = self.head.next
            if(p == None):
                return
            while(p != None):
                if(p.data != 0 and father_weight % p.data == 0):
                    p = self.tail
                    while(p != None):
                        if(p.data == 0 or father_weight % p.data != 0):
                            p.previous.next = None
                            self.tail = p.previous
                            lost_snakes.append(p.data)
                        else:
                            break
                        p = p.previous
                    break
                else:
                    if(p.next == None):
                        temp1 = self.head
                        temp2 = self.tail
                        self.head.data, self.tail.data = self.tail.data, self.head.data                       
                        break
                p = p.next
        
        lost_snakes.reverse()
        
        print(f"Play success!->{lost_snakes}")
        self.__str__()
        print("------------------------------")

    def  __str__(self):
        p = self.head
        if(p.next == None):
            print(f"({p.data})->Empty")
            return
        while(p != None):
            if(p == self.head):
                print(f"({p.data})", end="")
            else:
                print(p.data, end="")

            if(p.next != None):
                print(end="->")

            p = p.next
        
        print()

L = List()

inp = input("Snake Game : ").split("/")
snakes = inp[0].split()
actions = inp[1].split(",")

for snake in snakes:
    L.append(int(snake))

L.__str__()

for act in actions:
    if(act.split()[0] == "SW"):
        L.sw()
    elif(act.split()[0] == "SH"):
        L.sh()
    elif(act.split()[0] == "F"):
        L.f(int(act.split()[1]))
    elif(act.split()[0] == "D"):
        L.d(int(act.split()[1]))

if(L.head.next == None):
    print("Mom is dead")

print("Snake Game :")