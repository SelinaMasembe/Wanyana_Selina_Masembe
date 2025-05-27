#display information of classes person and subclasses student,lecturer and staff

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        
    def study(self):
        print(f"{self.name}  studies at the university.")
        
class Lecturer(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        
    def teach(self):
        print(f"{self.name} teaches at the university.")
        
class Staff(Person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self.staff_id = staff_id

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        
    def assist(self):
        print(f"{self.name} assists in the university operations.")
        
#create instances of each class and display
student = Student("Alice", 20, "S12345")
lecturer = Lecturer("Bob", 40, "E67890")
staff = Staff("Charlie", 35, "ST54321")

student.display_info()
student.study()
print()  

lecturer.display_info()
lecturer.teach()
print()

staff.display_info()
staff.assist()
print()

        
