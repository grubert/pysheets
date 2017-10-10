"""
Verzeichnis durch...laufen und ausgeben
"""

# unser test Verzeichnis
DIR="testdir"

print("mit prozeduralem Modul: os")
import os

print(os.listdir(DIR))

print("\nmit objektorientiertem Modul: pathlib")
import pathlib

# ein Objekt vom Verzeichnis/Pfad erzeugen 
dir = pathlib.Path(DIR)
# und alle Einträge ausgeben
for entry in dir.iterdir():
    print(entry)

# wenn man nur schnell den Inhalt sehen will ist os.listdir schneller
# wenn es formattiert sein soll
print("\nnoch einmal mit prozeduralem Modul: os")
for entry in os.listdir(DIR):
    print(entry)
# ist nicht mehr viel Unterschied
