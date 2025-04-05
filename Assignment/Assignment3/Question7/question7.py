import pandas as pd
import os
import csv

CSV_FILE = "employees.csv"
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
        write_header = not os.path.isfile(CSV_FILE) or os.stat(CSV_FILE).st_size == 0

        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(["Employee ID", "Name", "Address", "Contact", "Spouse", "Number of Children", "Salary"])
            writer.writerow([self.empid, self.name, self.address, self.contact, self.spouse, self.number_of_child, self.salary]) 

    def fetchdata(self):
        try: 
            df = pd.read_csv(CSV_FILE)
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
except Exception as e:
    print("Please enter a correct form of value", e)
    exit(0)

e1 = Employee(empid, name, address, contact,spouse, number_of_child, salary)
e1.intofile()
e1.fetchdata()