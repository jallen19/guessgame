#!/usr/bin/env python3
#guessgame.py
#James Allen
#10/30/17
#simple number guessing game

from random import randint
MIN = 1
MAX = 20


targetNumber = randint(MIN,MAX)

prompt = 'Please guesss a number from ' + str(MIN) + ' to ' + str(MAX) + ': '
guess = int(input(prompt))
print(guess)