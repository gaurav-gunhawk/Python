class Computer:

    def __init__(self,cpu=0,ram=0):
        self.c = cpu
        self.r  = ram


    def config(self):
        print(self.c)
        print(self.r)

c1 = Computer('i5',16)
c2 = Computer()
c1.config()
c2.config()

