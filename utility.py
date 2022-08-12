#!/usr/bin/python3
import os

def clear_screen():
    option = input("Input any letter to go back => ")
    if len(option) > 0:
        os.system("clear")
