from abc import ABC, abstractmethod

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self._department = department

    @abstractmethod
    def calc_bonus(self):
        pass

    @staticmethod
    def get_hours():
        return 8

    def get_department(self):
        return self._department.name

    def set_department(self, name, code):
        self._department = Department(name, code)


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1)) 

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self._sales = 0

    def get_sales(self):
        return self._sales

    def put_sales(self, sales):
        self._sales += sales
        return self._sales  

    def calc_bonus(self):
        return self._sales * 0.15
