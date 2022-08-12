#!/usr/bin/python3
import json
from expense import View, Expense
""" 
    Class Saving to save the data from the expense list

"""


class Saving:

    def __init__():
        pass

    @staticmethod
    def create_json(expenses):

        """ Take in parameters an expense list object to save it in a .json file """
        json_string = json.dumps([ob.__dict__ for ob in expenses])

        with open("student.json", "w") as file:
            #Writting object list elements in the json file

            file.write(json_string)
            print("Data saved successufully!!!")
        
    @staticmethod
    def retreiving_data(expenses):

        """ Take in parameter a .json file and load the data in a list of bject"""
        json_string = json.loads([ob.__dict__ for ob in expenses])
        print("Started writing list data into a json file")
        with open("student.json", "w") as file:
            file.write(json_string)
            print("Your data has been successfully loaded")
        
"""
    View.MenuView(Income)
        try:
            option = int(input("Select an Option: "))
        except ValueError:
            print("Only integer value are allowed!!")
            option = int(input("Please, try again. ==> "))

        if int(option) == 1:
            os.system('cls')
            View.ExpenseView(expenses)
            
            
        elif int(option) == 2: 
            os.system('cls')
            View.expense_add(expenses)
            
            
        elif int(option) == 3:
            os.system('cls')
            try:
                value = int(input("What is your income right now? ==> "))
            except ValueError:
                print("Only integer value are allowed!!")
                value = int(input("Please, try again. ==> "))
            Income = value
            print(f"Income set to {value} successfully.")
        
        elif int(option) == 4:
            os.system('cls')
            print("Started writing list data into a json file")
            Saving.create_json(expenses)
            
        elif int(option) == 5:
            os.system('cls')
            print("Loading your data")
            Saving.retreiving_data(expenses)
        
        elif int(option) == 6:
            exit(0)

        else:
            os.system('cls')
            continue
"""