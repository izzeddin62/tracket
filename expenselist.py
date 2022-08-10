#!/usr/bin/python3
from expense import Expense

expenses = [Expense('Rent', 300),Expense("leisure", 400)]

def expense_list():
    if len(expenses) == 0:
        print("You don't have any expense yet")
    else:
        print("these are your expenses:")
        for expense in expenses:
            print(f'{expense.get_name()}: {expense.get_value()}')


def expense_sum():
    summ = 0
    for expense in expenses:
        summ += expense.get_value()
    print("Your total expense:", summ)

def expense_add():
    print(f'You are adding a new expense')
    name = input("What is the expense name?:" )
    amount = int(input("How much have you spent?:" ))
    expenses.append(Expense(name, amount))
    print(f'Your expense has been recorded successfully.')
