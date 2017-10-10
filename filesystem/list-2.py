"""
Verzeichnis durch...laufen und ausgeben
"""

# unser test Verzeichnis
DIR="testdir"

print("mit prozeduralem Modul: os")
import os, os.path

for entry in os.listdir(DIR):
    if os.path.isdir(DIR+"/"+entry):
        print("DIR:"+entry)
    else:
        print(entry)

# man muss wissen, dass isdir in os.path ist, bzw. man muss es finden
# und man muss den Pfad komplett angeben : DIR+"/"+entry

print("\nmit objektorientiertem Modul: pathlib")
import pathlib

# ein Objekt vom Erzeugen 
dir = pathlib.Path(DIR)
# und alle Einträge ausgeben
for entry in dir.iterdir():
    # "entry" ist ein Objekt vom Typ "Path" und weisz selber, dass ob es ein Verzeichnis ist"
    if entry.is_dir():
        # entry ist kein String sondern ein Path und muss zum String gemacht werden
        print("DIR:"+str(entry))
    else:
        print(entry)


