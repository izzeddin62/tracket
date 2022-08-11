#!/usr/bin/python3
import expenselist
import os

def main_page(income=None):
    os.sys('cls')
    print("=====================================")
    print("=====================================")
    print(f"you have already spent {expenselist.sum()}")
    if income is not None:
        remaining = income - expenselist.sum()
        if remaining > 0:
            print(f"you are remaining with only {remaining}")
        elif remaining == 0:
            print("you have spent all your money. Be careful until you make more.")
        else:
            print(f"you are spending money you don't have. you already spent {remaining} you owe")
    print("=====================================")
    print("=====================================")
    print("HELLO WELCOME TO TRACKET\n")
    print("Choose an option\n")
    print("1.View my expense\n")
    print("2.Add new expense\n")
    print("3.add your income\n")
    print("4.Exit expenses\n")
    print("==================================")
    option = input("What do you want to do?")
    if int(option) == 1:
        expenselist.expense_list()
        main_page(income)
    elif int(option) == 2: 
         expenselist.expense_add()
         main_page(income)
    elif int(option) == 3:
       value = int(input("What is your income right now? "))
       income = value
       main_page(value) 
    elif int(option) == 4:
        exit(0)
    else:
        print("invalid input")
        main_page(income)


