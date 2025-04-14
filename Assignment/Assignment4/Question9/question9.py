'''
A program to manipulate data from csv file
'''

import pandas as pd
import numpy as np

#Creating a dataframe
df = pd.read_csv("data.csv")

#Function to select columns
def select(df):
    name = df['Name']
    salary = df['Salary']

    print(name,"\n", salary)

#Function to filter departments
def filter(df):
    filter = df[df['Department'] == 'IT']
    print(filter)

#Function to find older than 30 people from age column
def older(df):
    older = df[df['Age'] > 30]
    print(older)

#Function to find employees in each department and mean
def averageANDsize(df):
    departments = df['Department'].unique()
    
    for dep in departments:
        #calculate mean salary of each department
        avg = df[df['Department'] == dep]['Salary'].mean()
        print(f"Average Salary for department {dep} is {avg}")  

    #Calculate number of people in department
    department_counts = df.groupby('Department').size()
    print(department_counts)

#Function add bonus column
def bonus(df):
    df['Bonus'] = df['Salary']*0.10
    
    print(df)

#Function to replace 'HR' with 'Human Resources'
def replace(df):
    
    df['Department'] = df['Department'].replace('HR', "Human Resources")
    print(df)

#Function to find longest tenure
def tenure(df):
    df['JoinDate'] = pd.to_datetime(df['JoinDate'])

    # Find the earliest join date
    earliest_date = df['JoinDate'].min()

    # Filter employee(s) with that join date
    longest_tenure_employees = df[df['JoinDate'] == earliest_date]

    # Display the result
    print("Employee(s) with the longest tenure:")
    print(longest_tenure_employees)


#Function to create a new column to see if the salary is high or low
def SalaryCategory(df):
    # Create a new column based on Salary condition
    df['SalaryCategory'] = np.where(df['Salary'] > 75000, 'High', 'Low')
    print(df)

#Function to see if there is dublicate id and remove it
def filterID(df):
    duplicates = df[df['EmployeeID'].duplicated()]
    print("Duplicate EmployeeIDs:")
    print(duplicates)

    # Remove duplicates, keeping the first occurrence
    df_cleaned = df.drop_duplicates(subset='EmployeeID', keep='first')

    # Display the cleaned DataFrame
    print("\nData after removing duplicate EmployeeIDs:")
    print(df_cleaned)

#Function to calculate median age 
def agemedian(df):
    # Calculate the median age of all employees
    median_age = df['Age'].median()

    # Display the result
    print(f"The median age of all employees is: {median_age}")

#calling all function
select(df)
filter(df)
older(df)
averageANDsize(df)
bonus(df)
replace(df)
tenure(df)
SalaryCategory(df)
filterID(df)
agemedian(df)