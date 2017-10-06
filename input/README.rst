Einige Versuche zur Verwendung von input
========================================

Achtung:
--------

python2:

>>> input().__class__
3
<type 'int'>

python3:

>>> input().__class__
3
<class 'str'>

Was heisst das da oben ?

``>>>`` alles hinter diesem Zeichen tippt man in die Python-Shell ein.

  Die Python-Shell startet man durch den Aufruf von python.
  Unter Windows python.exe oder python2.exe oder python3.exe, oder im idle.

  Am mac oder linux python2 oder python3 auf der Kommandozeile.

``input()`` hier wird die Funktion input aufgerufen.

  Die Klammenr ``()`` bedeuten die FUnktion wird aufgerufen.
  Ohne Klammern bekommt man einen Verweis auf die Funktion.

  >>> input
  <built-in function input>
  >>> x = input
  >>> x("gib etwas ein:")
  gib etwas ein:4
  '4'

