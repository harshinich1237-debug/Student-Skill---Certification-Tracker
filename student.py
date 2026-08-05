class Student:
    def __init__(self, name, roll, dept):
        self.name=name
        self.roll=roll
        self.dept=dept
    def show(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Department:", self.dept)