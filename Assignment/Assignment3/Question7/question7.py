import pandas as pd
import csv
'''
A class emplyee with attributes and to write the data in a csv file 
Also, a function to fetch data from the file
It is done by importing two important libraries
'''

#Having global path for employees.csv
CSV_FILE = "employees.csv"
class Employee:
    #Constructor to initialize
    def __init__(self, empid, name, address, contact, spouse, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact = contact
        self.spouse = spouse
        self.number_of_child = number_of_child
        self.salary = salary

    #function to write into file
    def intofile(self):
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.empid, self.name, self.address, self.contact, self.spouse, self.number_of_child, self.salary]) 
    
    #function to fetch data from the file
    def fetchdata(self):
        try: 
            df = pd.read_csv(CSV_FILE)
            print(df)
        except Exception as e:
            print("Error opening file", e)


#Prompt user to get input with error handling
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

#Calling class instance
e1 = Employee(empid, name, address, contact,spouse, number_of_child, salary)

#Calling class function through instance
e1.intofile()
e1.fetchdata()