class Employee:
    def __init__(self,salary:float):
        if salary > 0:
            self .__salary = salary
        else:
            raise ValueError("Salary must be greater tha 0")

    def get_salary(self):
        print(f"Current salary:{self .__salary}")
        return float(self .__salary)
    def set_salary(self,new_salary:float):
        if new_salary > 0:
            self .__salary = new_salary
            print(f"Updated salary:{self .__salary}")
        else:
            print("Error:Salary mut be greater than 0")

employee =Employee(5000.0)
employee.get_salary()
employee.set_salary(6000.0)
employee.set_salary(-1000.0)