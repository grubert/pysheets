"""
Verzeichnis durch...laufen und ausgeben
"""

# unser test Verzeichnis
DIR="testdir"

import pathlib

print("A)")
# ein Objekt vom Verzeichnis/Pfad erzeugen 
dir = pathlib.Path(DIR)
# und alle Einträge ausgeben
for entry in dir.iterdir():
    if entry.is_dir():
        print(str(entry)+"/")
        for entry1 in entry.iterdir():
            if entry1.is_dir():
                print(str(entry1)+"/")
            else:
                print(entry1)
    else:
        print(entry)

# umbauen da der Code sich wiederholt
print("B)")
def print_dir(dir):
    for entry in dir.iterdir():
        if entry.is_dir():
            print(str(entry)+"/")
            print_dir(entry)
        else:
            print(entry)

print_dir(pathlib.Path(DIR))
