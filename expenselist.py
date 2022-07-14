#!/usr/bin/python3
expenses = []
def expense_list():
    if len(expenses) == 0:
        print("You don't have any expense yet")
    else:
        print("these are your expenses:")
        for expense in expenses:
            print(f'{expense[0]}: {expense[1]}')
