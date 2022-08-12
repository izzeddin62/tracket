from expense import View, Expense
from saving import Saving
from user import User
import os
import json

if __name__ == '__main__':
    
    Income = None
    expenses = [Expense('Rent', 300),Expense("leisure", 400)]
    users = [User("SANI", 20000), User("PRAISE", 120000), User("NINO", 50000), User("ELLSIE", 350000)]
    Bool = True
    
    User.IntroView()
    choice = int(input("Enter your option: "))
    Income = users[choice - 1].get_income()
    os.system('cls')

    while Bool:
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
        
    print("................................................................................................................................\n")

