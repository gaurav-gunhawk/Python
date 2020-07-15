from abc import ABC,abstractmethod
# When inherting any abstract class its compulsory to define all the methods of abstract class into the child class.
class Computer(ABC):
    @abstractmethod
    def start(self):
        pass

class Laptop(Computer): # Inheriting abstract class and using its functions declaration
    def start(self):
        print("Starting")

l1 = Laptop()
l1.start()