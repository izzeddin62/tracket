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

def expense_add():
    print(f'You are adding a new expense')
    name = input("What is the expense name?:" )
    amount = int(input("How much have you spent?:" ))
    expenses.append((name, amount))
    print(f'Your expense has been recorded successfully.')
