'''
A student class to get value from user and give output of all the data
'''

#defining class
class Student:
    #Using __init__ constructor to initialize value
    def __init__(self, id, name, address, year, lvl, sec):
        self.id = id
        self.name = name
        self.address = address
        self.year = year
        self.level = lvl
        self.section = sec

    #This function prints our all the input in user-friendly manner
    def giveOutput(self):
        print(f"Name: {self.name}")
        print(f"Id: {self.id}")
        print(f"address: {self.address}")
        print(f"year: {self.year}")
        print(f"level: {self.level}")
        print(f"Section: {self.section}")


#Prompt user to get following data
id = input("Enter your ID: ")
name = input("Enter your name: ")
address = input("Enter your address: ")
year = input("Enter your year: ")
level = input("Enter your level: ")
section = input("Enter your section: ")

#creating class instance
s1 = Student(id, name, address, year, level, section)
#calling class function
s1.giveOutput()