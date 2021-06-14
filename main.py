# This is a sample Python script.
from pymongo import MongoClient
import pprint
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


client = MongoClient()

#create database
db = client.javatpoint

employee = {"id": "101",
"name": "Peter",
"profession": "Software Engineer",}

employees = db.employees

#insert data

employees.insert_one(employee)

#fetch data

pprint.pprint(employees.find_one())


#create document


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
