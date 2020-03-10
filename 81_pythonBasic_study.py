#! /usr/bin/python2.7
# function: remove next duplicate in array.

class PhysicalMemoryCtrl(object):
    def currentAddr(self):
        print("KK_____ currentAddr")
        return self.__currentAddr

    def __init__(self, initAddr):
        print("KK_____ __init__")
        self.__currentAddr = initAddr

print("KK_____000000001")
addr = 0xfd000000
print("KK_____000000002")
#a = PhysicalMemoryCtrl(initAddr=addr)
a = PhysicalMemoryCtrl(addr)
print("KK_____000000003")
rst = a.currentAddr()
print("KK_____000000004")
print("0x%x " % rst)

print("=====================================================")
print("=====================================================")
class   Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def name(self):
        return self.firstname + " " + self.lastname

class   Employee(Person):
    def __init__(self, firstname, lastname, staffId):
        Person.__init__(self, firstname, lastname)
        #super().__init__(firstname, lastname)
        self.staffId = staffId

    def info(self):
        return "Employee : " + self.name() + ", " + str(self.staffId)


class Employer(Person):
    def __init__(self, firstname, lastname, position):
        Person.__init__(self, firstname, lastname)
        #super().__init__(firstname, lastname)
        self.position = position

    def info(self):
        return "Employee : " + self.name() + ", " + self.position

worker = Employee("kenny", "kwak", 3712)
cfo = Employer("t", "y", "ceo")
print(worker.info())
print(cfo.info())

print("=====================================================")
print("=====================================================")
class Computer():
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super(Laptop, self).__init__(computer, ram, ssd)
        self.model = model

lenovo = Laptop('lenovo', 2, 512, 'l420')
print('This computer is:', lenovo.computer)
print('This computer has ram of', lenovo.ram)
print('This computer has ssd of', lenovo.ssd)
print('This computer has this model:', lenovo.model)