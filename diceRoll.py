# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 10:32:21 2018

@author: tbieleni
"""

from random import randint

print("Welcome in dice roller!")

def diceRoll():
    hand = input("Pick dice type and quantity e.g. 2D6: ").lower()
    d = hand.index("d")
    if d == 0:
        dQty = 1
    else:
        dQty = int(hand[:d])
    dT = int(hand[d+1:])
    outcome = 0
    for i in range(int(dQty)):
        score = randint(1,dT)
        print(score)
        outcome += score
    print("Your outcome is: "+ str(outcome))
    
    oneMore = input("One more roll? (y/n): ")
    if oneMore.lower() == "y":
        diceRoll()
    else:
        print()

diceRoll()
