
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
            try:
                value = int(input("What is your income right now? ==> "))
            except ValueError:
                print("Only integer value are allowed!!")
                value = int(input("Please, try again. ==> "))
            Income = value
            print(f"Income set to {value} successfully.")
            
        elif int(option) == 4:
            exit(0)