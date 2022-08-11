#!/usr/bin/python3
from expense import Expense
import os
from utility import clear_screen

expenses = [Expense('Rent', 3000),Expense("Leisure", 1000)]

def expense_list():
    os.system('clear')
    if len(expenses) == 0:
        print("You don't have any expense yet.")
    else:
        print("These are your expenses.")
        for expense in expenses:
            print(f'{expense.get_name()}: {expense.get_value()}')
    clear_screen() 
def sum():
    summ = 0
    for expense in expenses:
        summ += expense.get_value()
    return summ

def expense_add():
    print(f'You are adding a new expense.')
    name = input("What is the expense name?: ==> " )
    try:
        amount = int(input("How much have you spent?: ==> " ))
    except ValueError:
        print("Only integer value are allowed")
        amount = int(input("Try again. ==>"))
    expenses.append(Expense(name, amount))
    print(f'Your expense has been recorded successfully.')
    clear_screen() 
