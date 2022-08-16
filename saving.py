#!/usr/bin/python3
import json
from expense import View, Expense
""" 
    Class Saving to save the data from the expense list
"""


class Saving:

    def __init__():
        pass

    @staticmethod
    def to_json(dict_list):
        if len(dict_list) == 0:
            return "[]"
        return json.dumps(dict_list)

    @staticmethod
    def save_to_file(expenses):
        list_dict = [i.to_dictionary() for i in expenses]
        with open("student.json", 'w', encoding="utf-8") as f:
            f.write(Saving.to_json(list_dict))

    @staticmethod
    def create_json(e):

        """ Take in parameters an expense list object to save it in a .json file """
        json_string = json.dumps([ob.__dict__ for ob in expenses])

        with open("student.json", "w") as file:
            #Writting object list elements in the json file

            file.write(json_string)
            print("Data saved successufully!!!")
        
    @staticmethod
    def retreiving_data(): 
        with open("student.json", "r", encoding='utf-8') as file:
            dict_list = json.loads(file.read())
            expenses = [Expense(i['name'], i['value']) for i in dict_list]
        return expenses;