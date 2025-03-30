class Student:
    def __init__(self, id, name, address, year, lvl, sec):
        self.id = id
        self.name = name
        self.address = address
        self.year = year
        self.level = lvl
        self.section = sec

    def giveOutput(self):
        print(f"Name: {self.name}")
        print(f"Id: {self.id}")
        print(f"address: {self.address}")
        print(f"year: {self.year}")
        print(f"level: {self.level}")
        print(f"Section: {self.section}")


id = input("Enter your ID: ")
name = input("Enter your name: ")
address = input("Enter your address: ")
year = input("Enter your year: ")
level = input("Enter your level: ")
section = input("Enter your section: ")
s1 = Student(id, name, address, year, level, section)
s1.giveOutput()