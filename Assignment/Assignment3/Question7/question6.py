import pandas as pd

class Employee:
    def __init__(self, empid, name, address, contact, spouse, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact = contact
        self.spouse = spouse
        self.number_of_child = number_of_child
        self.salary = salary

    def intofile(self):
        file = open("employees.csv", "a+")
        file.write(f"{self.empid, self.name, self.address, self.contact, self.spouse, self.number_of_child, self.salary}\n") 
        file.close() 
def getdata():
    try: 
        df = pd.read_csv("employees.csv")
        print(df)
    except Exception as e:
        print("Error opening file", e)

try:
    empid = int(input("Enter the employee id: "))
    name = str(input("Enter the employee name: "))
    address = str(input("Enter the employee address: "))
    contact = str(input("Enter the employee contact: "))
    spouse = str(input("Enter the employee spouse: "))
    number_of_child = int(input("Enter the number of child employee has: "))
    salary = float(input("Enter the salary of employee: "))
except ValueError as v:
    print("Please enter a correct form of value", v)

e1 = Employee(empid, name, address, contact,spouse, number_of_child, salary)
e1.intofile()

getdata()