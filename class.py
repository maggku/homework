"""
Exercise 1: Employee Factory
Create an Employee class with:

Attributes: name, salary, position
A method info() that prints the employee details
A factory class method from_hourly_rate(cls, name, hourly_rate,
hours_per_month) that calculates monthly salary and creates an employee
with position "Hourly Worker"

Then create:

One employee directly with a monthly salary
One employee using the factory method

Expected output:

Alice - Manager - Salary: 5000
Bob - Hourly Worker - Salary: 3200
"""


class Employee():
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def info(self):
        print(f"{self.name} - {self.position} - Salary: {self.salary}")

    @classmethod
    def from_hourly_rate(cls, name, hourly_rate, hours_per_month):
        monthly_salary = hours_per_month * hourly_rate
        hourly_worker = cls(name, monthly_salary, "Hourly Worker")
        return hourly_worker


employee1 = Employee("Alice", "5000", "Manager")
employee1.info()

employee2 = Employee.from_hourly_rate("Bob", 20, 160)
employee2.info()

"""
Exercise 2: Book Factory Functions
Create a Book class with:

Attributes: title, author, year, genre
A method info() that prints book details

Then create TWO separate factory functions:

create_classic_book(title, author, year) - creates a book with genre "Classic"
create_scifi_book(title, author, year) - creates a book with genre "Science Fiction"

Create 2 books using these factories and display their info.
Expected output:

"""