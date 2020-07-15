class Outerclass:  # Outer class
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    class Innerclass: # class inside a class is called inner class
        def __init__(self):
            print("check")


s1 = Outerclass('gaurav', 12)
lap = Outerclass.Innerclass()  # Creating object of an inner class

print(s1.name , s1.rollno)
