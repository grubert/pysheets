Arbeiten mit dem Dateisystem -- und warum Objekte
=================================================

Das Dateisystem, die Platte, gehört zum Betriebssystem, deshalb passiert
der Zugriff über das Module os.

``os.listdir(".")`` gibt eine Liste/Array mit den Namen der Einträge im 
derzeitigen Verzeichnis (das Konzept des current directory ist in einer GUI
etwas verschleiert).

Um herauszufinden welche Einträge ein Verzeichnis sind benutzt man die Funktion
``isdir`` aus dem Modul ``os.path``

>>>
import os, os.path
for direntry in os.listdir("."):
    if os.path.isdir(direntry):
        print(direntry+" ist ein Verzeichnis")

``os.listdir(".")`` gibt die Liste zurück und dir for-Schleife arbeitet
diese schrittweise, Eintrag für Eintrag, ab.

In Python3 gibt es das Modul ``pathlib`` zur Arbeit mit Pfaden.

>>>
for path in pathlib.Path(".").iterdir():
    if path.is_dir(): 
        print(str(path)+" ist ein Verzeichnis")

``pathlib.Path(".")`` erzeugt ein Objekt das ... eine Schnittstelle zum
current directory "." ist. Was das genau ist ist mir persönlich egal.
``iterdir()`` ist eine Funktion/Methode dieses Objektes die mir erlaubt
alle Einträge aufzulisten.

``iterdir`` ist ein Iterator, das heißt es wird bei jedem Aufruf nur ein
Eintrag zurückgegeben.

Das hat Vorteile wenn über 10Millionen Einträge eingelesen werden, weil
dann nicht alle 10 Millionen im Speicher sein müssen.

Das hat den Nachteil, dass man nicht sortieren kann. Das kann man nur wenn 
man alle Einträge hat.

``iterdir`` gibt jeweils einen Eintrag vom Typ/Class Path zurück, das heisst
man kann vom Eintrag durch Aufruf der Methode ``.is_dir()`` erfahren ob er
ein Verzeichnis ist.

Man kann den Eintrag dann auch gleich mit ``path.iterdir()`` um seine Einträge 
Fragen.

Bei ``os.listdir`` muss man den Pfad als Zeichenkette/String übergeben, das heisst wenn ich die Einträge in einem Unterverzeichnis haben will muss ich den Namen
des darüberliegenden berücksichtigen, siehe os.path.join etc.

Code
----

Wir machen uns einen Verzeichnisbaum zum ausprobieren ... gleich mit python

>>>
import pathlib
# alles mit / am Ende is ein Verzeichnis
testdirs = (
    "testdir/",
    "testdir/index.txt",
    "testdir/doc/",
    "testdir/doc/index.txt",
    "testdir/doc/liesmich.txt",
    "testdir/doc/mans/",
    "testdir/doc/mans/liesmich.txt",
    "testdir/py/",
    "testdir/py/index.txt",
    "testdir/py/nothing.py",
    "testdir/py/todo.py",
    "testdir/txt/",
    "testdir/txt/index.txt",
    "testdir/txt/index.txt",
    )
#
for e in testdirs:
    p = pathlib.Path(e)
    if p.exists():
        continue
    if e.endswith("/"):
        p.mkdir()
    else:
        p.touch()


muss ja nicht gleich jeder verstehen.    
