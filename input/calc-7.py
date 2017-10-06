"""
allgemeiner rechner
"""
import readline
from math import *

while True:
    s = input(":-> ")
    if s.strip() == "":
        print("bye")
        break
    print(eval(s))

