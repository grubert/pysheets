"""
allgemeiner rechner
"""
import readline

while True:
    s = input(":-> ")
    if s.strip() == "":
        print("bye")
        break
    print(eval(s))

