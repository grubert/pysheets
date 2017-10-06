"""
nur deziamlwerte akzeptieren, dann addieren
"""
while True:
    a = input("bitte ersten wert eingeben: ")
    if a.isdecimal():
        a = int(a)
        break
    else:
        print("bitte eine zahl eingeben")
while True:
    b = input("bitte zweiten wert eingeben: ")
    if b.isdecimal():
        b = int(b)
        break
    else:
        print("bitte eine zahl eingeben")
c = a + b
print(c)
