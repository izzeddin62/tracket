#!/usr/bin/python3
from expense import View, Expense
from saving import Saving
from user import User
import os
import json

if __name__ == '__main__':

    Income = None
    expenses = Saving.retreiving_data()
    users = [User("SANI", 20000), User("PRAISE", 120000), User("NINO", 50000), User("ELLSIE", 350000)]
    Bool = False
    choice = None

    User.IntroView()
    while Bool == False:
        if choice is not range(1,5):
            choice = int(input("Enter your option: "))
            Income = users[choice - 1].get_income()
            Bool = True
    os.system('clear')
    while Bool:
        
        View.MenuView(Income, expenses)
        try:
            option = int(input("Select an Option: "))
        except ValueError:
            print("Only integer value are allowed!!")
            option = int(input("Please, try again. ==> "))

        if int(option) == 1:
            os.system('clear')
            View.ExpenseView(expenses)
            
            
        elif int(option) == 2: 
            os.system('clear')
            View.expense_add(expenses)
            Saving.save_to_file(expenses)
            print("\n\n")
            input("Enter any key .......")
            os.system('clear')
            
        elif int(option) == 3:
            os.system('clear')
            try:
                value = int(input("What is your income right now? ==> "))
            except ValueError:
                print("Only integer value are allowed!!")
                value = int(input("Please, try again. ==> "))
            Income = value
            print(f"Income set to {value} successfully.")
        
        elif int(option) == 4:
            os.system('clear')
            print("Loading your data")
            #Saving.retreiving_data(expenses)
        
        elif int(option) == 5:
            exit(0)

        else:
            os.system('clear')
            continue
        
    print("................................................................................................................................\n"