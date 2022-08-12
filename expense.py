#!/usr/bin/python3
from time import sleep
from uuid import uuid4

from tabulate import tabulate
import os

class Expense:
    """ Creating the expense class """

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.id = str(uuid4())
    
    """ getter method """
    def get_name(self):
        return self.name

    def get_value(self):
        return self.value
        
    """ setter method """
    def set_value(self, x):
        self.name = x
    
    def set_name(self, y):
        self.value = y


expenses = [Expense('Rent', 300),Expense("leisure", 400)]

class View():
    """ Creating the view class """
    def __init__(self):
        pass

    @staticmethod
    def ExpenseView(expenses):
        data = [[i.name, i.value] for i in expenses]
        print(data)
        os.system('clear')
        if len(expenses) == 0:
            print("You don't have any expense yet.")
        else:
            print("These are your expenses.\n\n")
            #for expense in expenses:
                #print(f'{expense.get_name()}: {expense.get_value()}')
            print(tabulate(data, headers= ['NAME', 'VALUE']))
            print("\n\n")
            input("Enter any key .......")
            os.system('clear')
    
    @staticmethod
    def Sum():
        summ = 0
        for expense in expenses:
            summ += expense.get_value()
        return summ

    @staticmethod
    def SumView():
        print(f"Your total expense:{sum()}")


    @staticmethod
    def expense_add(expenses):
        print(f'You are adding a new expense')
        name = input("What is the expense name?:" )
        amount = int(input("How much have you spent?:" ))
        expenses.append(Expense(name, amount))
        print(f'Your expense has been recorded successfully.')


    @staticmethod
    def MenuView(income):

        """ Display of Menu and differents options """
        print("-----------------------------------------------")
        print("-----------------------------------------------")

        print(f"You have already spent {View.Sum()}")

        if income is not None:
            remaining = income - View.Sum()

            if remaining > 0:
                print(f"You are remaining with only {remaining}.")

            elif remaining == 0:
                print("You will run out of money.\nLearn to spend wisely!!")

            else:
                print(f"You are running on a budget.\nYou already spent {remaining} above your budget.")

        print("-------------------------------------------------")
        print("-------------------------------------------------")
        print("         HELLO, WELCOME TO TRACKET!!\n")
        print("         Choose an option\n")
        print("         1-View your expenses\n")
        print("         2-Add a new expense\n")
        print("         3-Add your new income\n")
        print("         4-Retrieve all the expenses\n")
        print("         5-Exit\n")
        print("-------------------------------------------------")
    

    
