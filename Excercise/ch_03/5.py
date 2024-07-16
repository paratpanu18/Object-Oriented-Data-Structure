class ArrayStack:
    def __init__(self, size: int = None):
        self.data = []
        self.size = size

    def push(self, d):
        if self.size and len(self.data) == self.size:
            return False
        
        self.data.append(d)
        return True

    def pop(self) -> any:
        return self.data.pop()

    def top(self) -> any:
        return self.data[-1]
    
    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def clear(self):
        self.data = []

print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)

parking_lot = ArrayStack(m)

if len(s) > 0:
    for car in s.split(','):
        if int(car) != 0 and not parking_lot.push(int(car)):
            print(f'car {car} cannot arrive : Soi Full')
            exit()

# print(f'car in soi : {parking_lot.data if not parking_lot.isEmpty() else "Empty"}')

if o == 'arrive':
    if not parking_lot.isEmpty() and n in parking_lot.data:
        print(f'car {n} already in soi')
    else:
        if not parking_lot.push(n):
            print(f'car {n} cannot arrive : Soi Full')
        else:
            print(f'car {n} arrive! : Add Car {n}')

elif o == 'depart':
    if parking_lot.isEmpty():
        print(f'car {n} cannot depart : Soi Empty')
    elif n not in parking_lot.data:
        print(f'car {n} cannot depart : Dont Have Car {n}')
    else:
        print(f'car {n} depart ! : Car {n} was remove')
        parking_lot.data.remove(n)

print(parking_lot.data if not parking_lot.isEmpty() else [])