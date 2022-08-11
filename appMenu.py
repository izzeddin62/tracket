#!/usr/bin/python3
import expenselist
import os
from utility import clear_screen

def main_page(income=None):
    print("=====================================")
    print("=====================================")
    print(f"You have already spent {expenselist.sum()}")
    if income is not None:
        remaining = income - expenselist.sum()
        if remaining > 0:
            print(f"You are remaining with only {remaining}.")
        elif remaining == 0:
            print("You have spent all your money.\n Be careful until you make more.")
        else:
            print(f"You are running on a budget.\n You already spent {remaining} above your budget.")
    print("=====================================")
    print("=====================================")
    print("HELLO, WELCOME TO TRACKET!!\n")
    print("Choose an option\n")
    print("1.View your expenses\n")
    print("2.Add new expense\n")
    print("3.Add your income\n")
    print("4.Exit expenses\n")
    print("==================================")
    option = input("What do you want to do? ==> ")
    if int(option) == 1:
        expenselist.expense_list()
        main_page(income)
    elif int(option) == 2: 
         expenselist.expense_add()
         main_page(income)
    elif int(option) == 3:
        try:
            value = int(input("What is your income right now? ==> "))
        except ValueError:
            print("Only integer value are allowed!!")
            value = int(input("Please, try again. ==> "))
        income = value
        print(f"Income set to {value} successfully.")
        clear_screen()
        main_page(value) 
    elif int(option) == 4:
        exit(0)
    else:
        print("Invalid input")
        main_page(income)


