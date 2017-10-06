"""
nur deziamlwerte akzeptieren, dann addieren

refactor = aufräumen
"""
werte = [0, 0]
for i in range(2):
    txt = ("ersten", "zweiten")[i]
    while True:
        a = input("bitte ersten "+txt+" eingeben: ")
        if a.isdecimal():
            werte[i] = int(a)
            break
        else:
            print("bitte eine zahl eingeben")
c = werte[0] + werte[1]
print(c)
