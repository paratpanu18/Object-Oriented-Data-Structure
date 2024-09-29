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

class Department:
    def __init__(self, name: str, employees: list = None) -> None:
        self.department_name: str = name
        self.employee: list = employees if employees else []

    def add_employee(self, name):
        self.employee.append(name)

class DepartmentQueue(Queue):
    def __init__(self, department: str, lst: list = None) -> None:
        super().__init__(lst)
        self.department = department
class Canteen:
    def __init__(self, employees) -> None:
        self.queue: Queue = Queue()
        self.departments: list = []

        for employee in employees:
            department_name, name = employee.split()
            department = self.get_department_by_name(department_name)

            if not department:
                self.departments.append(Department(department_name, [name]))
            else:
                department.add_employee(name)
    
    def run(self, commands: str) -> None:
        return "\n".join(filter(None, (self.perform_operation(command) for command in commands.split(','))))
        
    def perform_operation(self, command: str) -> str:
        if command.startswith('E'):
            _ , employee = command.split()
            department = self.get_department_of_employee(employee)

            '''
                Don't have department queue in current queue
                So, create new department queue and add employee

                However, if department queue already exists, add employee to that department queue
            '''

            department_queue = self.get_department_queue(department.department_name)
            if not department_queue:
                self.queue.enQueue(DepartmentQueue(department.department_name, [employee]))
            else:
                department_queue.enQueue(employee)

        elif command.startswith('D'):
            '''
                If queue is not empty, dequeue the first employee from the first department queue
                If department queue is empty, print "Empty
            '''

            if not self.queue.isEmpty():
                department_queue = self.queue.head()
                employee = department_queue.deQueue()

                if department_queue.isEmpty():
                    self.queue.deQueue()

                return employee
            
            else:
                return "Empty"

    def get_department_queue(self, department: str) -> DepartmentQueue:
        for queue in self.queue.getQueue():
            if queue.department == department:
                return queue
        return None
    
    def get_department_by_name(self, department_name: str) -> Department | None:
        for department in self.departments:
            if department.department_name == department_name:
                return department
        return None
    
    def get_department_of_employee(self, employee: str) -> str:
        for department in self.departments:
            if employee in department.employee:
                return department
        return None

employees, operations = input('Enter Input : ').split('/')
employees: list = employees.split(',')

app: Canteen = Canteen(employees)
print(app.run(operations))