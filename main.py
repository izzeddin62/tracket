#!/usr/bin/python3
import expenselist
def main_page():
    print("HELLO WELCOME TO TRACKET\n")
    print("Choose an option\n")
    print("1.View my expense\n")
    print("2.Add new expense\n")
    print("3.Total expenses\n")
    option = input("What do you want to do?")
    if int(option) == 1:
        expenselist.expense_list()
        main_page()
    elif int(option) == 2: 
         expenselist.expense_add()
         main_page()
    elif int(option) == 3:
        expenselist.expense_sum()
        main_page()
    else:
        print("invalid input")
        main_page()

main_page()
