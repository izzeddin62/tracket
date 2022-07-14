#!/usr/bin/python3
expenses = [('Rent', 300),("leisure", 400)]

def expense_list():
    if len(expenses) == 0:
        print("You don't have any expense yet")
    else:
        print("these are your expenses:")
        for expense in expenses:
            print(f'{expense[0]}: {expense[1]}')


def expense_sum():
    summ = 0
    for s in expenses:
        summ += s[1]
    print("Your total expense:", summ)

