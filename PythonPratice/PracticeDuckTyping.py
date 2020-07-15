from ctypes import PyDLL


class Pycharm:
    def execute(self):
        print("Pycharm")

class Eclipse:
    def execute(self):
        print("Eclipse")

class Ide:
    def code(self,ide):# in ide we can pass any object unlike other languages,because we are not specifying any type here
        ide.execute()  # That class must have that function that is called over here.

idObj = Ide()
py = Pycharm()

idObj.code(py)