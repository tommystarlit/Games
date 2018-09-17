# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 10:32:21 2018

@author: tbieleni
"""

print("Welcome in dice roller!")
from random import randint

def diceRoll():
    qty = input("How many D6 would you like to roll?: ")
    outcome = 0
    for i in range(int(qty)):
        score = randint(1,6)
        print(score)
        outcome += score
    print("Your outcome is: "+ str(outcome))
    print()
    diceRoll()
    
diceRoll()
