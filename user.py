#!/usr/bin/python3
class User:
    def __init__(self, name, income):
        self.name = name
        self.income = income

    """ getter method """
    def get_name(self):
        return self.name

    def get_income(self):
        return self.income
        
    """ setter method """
    def set_income(self, x):
        self.name = x
    
    def set_name(self, y):
        self.income = y

    @staticmethod
    def IntroView():
        print("                     T-R-A-C-K-E-T          ")
        print(" \x1B[3m     Your favourite expenses tracker buddy...  \x1B[0m \n")  

        print("  WELCOME AND THANKS FOR PARTICIPATING IN OUR APP TESTING PHASE")
        print("             Before starting please select a user\n")
        print("             1. Name: SANI      Income: 20000")
        print("             2. Name: PRAISE    Income: 120000")
        print("             3. Name: NINO      Income: 50000")
        print("             4. Name: ELLSIE    Income: 350000")




