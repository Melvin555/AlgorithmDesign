import datetime
my_date = datetime.date(2017, 7, 3)

class Employee:
    rise = 1.04
    
    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.py = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    
    def pay_rise(self):
        self.py = self.py * self.rise
        
    @classmethod
    def set_rise(cls, amount):
        cls.rise = amount
        
    @classmethod
    def from_string(cls, emp_str):
        fname, lname, py = emp_str.split('-')
        return cls(fname, lname, py)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
#using dunder
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.fname, self.lname, self.py)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.py + other.py
        
class Developer(Employee):
    
    rise = 1.10
    
    def __init__(self, first, last, pay, prog_lg):
        super().__init__(first, last, pay)
        self.prog = prog_lg

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

#---------------------------------------------------------------

dev_1 = Developer('Christ', 'Redfield', 80000, 'Python')
dev_2 = Developer('Mutan', 'Gargantua', 85000, 'C++')

emp_1 = Employee('Melvin', 'Harsono', 70000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'Alexander-Halim-70000'
emp_str_2 = 'Vanny-Febriana-50000'

emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)

mgr_1 = Manager('Sue', 'Sminth', 100000, [dev_1])

#---------------------------------------------------------------

#print(isinstance(mgr_1, Developer))
#print(issubclass(Developer, Employee))

print(emp_1.fullname())
print(Employee.fullname(emp_1))
print()
print(emp_1.py)
Employee.pay_rise(emp_1)
print(emp_1.py)
print(emp_1.rise)
print()
Employee.set_rise(1.05)
print(emp_1.rise)
print()
print(emp_3.email)
print()
print(Employee.is_workday(my_date))
print()
print(dev_1.email)
print(dev_1.prog)
print()
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
print()
#after using dunder
print(emp_1)
print(emp_1+emp_2)