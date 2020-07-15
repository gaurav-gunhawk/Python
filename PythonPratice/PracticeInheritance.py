class A:
    def __init__(self):
        print("In A")

class B:
    def __init__(self):
        super().__init__()  # Calling parent class
        print("In  b")

    def show(self):
        print("In B")


class C(A,B):
    def __init__(self):
        pass
s1 = C()