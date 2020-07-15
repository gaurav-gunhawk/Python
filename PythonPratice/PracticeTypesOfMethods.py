# Instance methods
# Class Methods
# Static methods

class Student:

    school = 'Programming School'  # static or class variable

    def __init__(self , m1 , m2 , m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):    # instance method
        return (self.m1 + self.m2 + self.m3)/3

    def avg(self):
        return self.m1

    @classmethod      # Annotation used for declaring class method
    def info(cls):    # class method
        return cls.school

    @staticmethod     # Annotation used for declaring static method
    def extra():      # static method
        print("This is Static Method")

s1 = Student(12,54,87)
s2 = Student(56,23,31)

print(s1.avg())
print(Student.info())
Student.extra()