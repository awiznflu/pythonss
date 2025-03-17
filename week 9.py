class Pet:
    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # Getter methods
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

# Create a Pet object and interact with it
pet = Pet()

# Get user input for pet details
pet.set_name(input("Enter your pet's name: "))
pet.set_animal_type(input("Enter your pet's animal type (Dog, Cat, Bird, etc.): "))
pet.set_age(int(input("Enter your pet's age: ")))

# Display the pet's details
print(f"Pet's Name: {pet.get_name()}")
print(f"Animal Type: {pet.get_animal_type()}")
print(f"Pet's Age: {pet.get_age()}")

class Person:
    def __init__(self, name="", address="", age=0, phone_number=""):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # Getter methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

class Employee(Person):
    def __init__(self, name="", address="", age=0, phone_number="", department="", pay_rate=0.0, shift=""):
        # Initialize the base class (Person)
        super().__init__(name, address, age, phone_number)
        self.__department = department
        self.__pay_rate = pay_rate
        self.__shift = shift

    # Setter methods
    def set_department(self, department):
        self.__department = department

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    # Getter methods
    def get_department(self):
        return self.__department

    def get_pay_rate(self):
        return self.__pay_rate

    def get_shift(self):
        return self.__shift

# Create three instances of the Employee subclass
employee1 = Employee("John Doe", "123 Elm St", 30, "555-1234", "Engineering", 25.50, "Morning")
employee2 = Employee("Jane Smith", "456 Oak St", 28, "555-5678", "HR", 22.00, "Afternoon")
employee3 = Employee("Alice Johnson", "789 Pine St", 35, "555-8765", "Marketing", 27.00, "Night")

# Display details for each employee
employees = [employee1, employee2, employee3]

for emp in employees:
    print(f"Name: {emp.get_name()}")
    print(f"Address: {emp.get_address()}")
    print(f"Age: {emp.get_age()}")
    print(f"Phone: {emp.get_phone_number()}")
    print(f"Department: {emp.get_department()}")
    print(f"Pay Rate: ${emp.get_pay_rate()}/hr")
    print(f"Shift: {emp.get_shift()}")
