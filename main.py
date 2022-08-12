from expense import View, Expense
import os
import json

if __name__ == '__main__':
    Income = None
    expenses = [Expense('Rent', 300),Expense("leisure", 400)]
    Bool = True
    
    print("............................T......R.....A......C........K........E........T...................................................\n")
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

            print("Started writing list data into a json file")
            with open("expenses.json", "w") as fp:
                json_data = json.dump(expenses, fp)
                print("Done writing JSON data into .json file")
            
        elif int(option) == 5:
            exit(0)
        else:
            os.system('cls')
            continue
        
    print("...........................................................................................................................\n") 
