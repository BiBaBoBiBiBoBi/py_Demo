class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"employee name:{self.name}\nemployee id:{self.id}")

    def calculate_monthly_pay(self):
        print(f"calculate_monthly_pay for {self.name}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        super().calculate_monthly_pay()
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        super().calculate_monthly_pay()
        return self.work_days * self.daily_salary


john = FullTimeEmployee("john", 1011, 10400)
lee = PartTimeEmployee("lee", 2101,120,15)

john.print_info()
lee.print_info()
print(john.calculate_monthly_pay())
print(lee.calculate_monthly_pay())
