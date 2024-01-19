# 1.
# a. Geben sei eine Textdatei mit dem Namen "people.txt" an, die in jeder Zeile zwei Werte enthalt,
# eine Zeichenkette (der Name einer Person) und eine Zahl (das Alter der Person), getrennt durch
# eine Komma ",", schreiben Sie eine Funktion "count_palindromes", die:
#       -einen Parameter names "underage" enthält
#       -einen Parameter für den Namen der Datei enthält
#       -aus der angegebenen txt-Datei "people.txt" liest

# Die Funktion zählt die Personen in der Datei, deren Name ein Palindrom ist.
# Die Berechnung erfolgt nach folgenden Regeln:
#     1. Wenn "underage" True ist, zählt man die Personen, deren Name ein Palindrom ist,
#     die minderjährig sind
#     2. Wenn "underage" False ist, zählt man alle Personen, deren Name ein Palindrom ist

# Es wird erwartet, dass die Lösung map, filter oder reduce und andere mathematische
# Operationen, falls erforderlich, benützt.

# Beispiel für people.txt
#       -underage + palindrom:  2
#       -all names that are palindromes:  6

# b. Schreiben Sie 2 Testfälle für die Funktion (einen für 'underage=True' und einen für 'underage=False')


# 2.
# a. Es wird die Klasse BinaryNumber angegeben, die eine Zeichenfolge aus 0 und 1 enthält, die bei der
# Erstellung des Objekts an die Klasse gesendet wird. Auf der Grundlage dieser Zeichenkette wird im
# Konstruktor eine Liste erstellt, in die jede Ziffer der Zeichenkette eingetragen wird.
# Schreiben Sie eine Funktion "sum", die zwei BinaryNumber-Objekte auf der Grundlage ihrer Liste
# addiert. Die beiden Zahlen können unterschiedliche Längen haben.

# Fügen Sie der Funktion einen Parameter "return_list" hinzu, der bestimmt, was die Funktion zurückgibt.
#       1. Wenn "return_list" True ist, gibt die Funktion die Binärzahl als Liste zurück.
#       2. Wenn "return_list" False ist, gibt die Funktion die Binärzahl als String zurück.

# Beispiel:
#       binary_number1 = BinaryNumber("101")
#       binary_number2 = BinaryNumber("1110")
#       res_sum = binary_number1.sum(binary_number2, return_list=False)
#       res_sum = binary_number1.sum(binary_number2, return_list=True)

# b.
# Erstellen Sie die Klasse RepoBinaryNumber number, die als Attribut eine Liste von BinaryNumber-Objekten hat.
# Schreibe eine Funktion "sum_all", die die Summe der ungeraden Zahlen zurückgibt. Bemerkungen:
#   1. Verwenden Sie die in Punkt a) definierte Funktion
#   2. Nur die mit der Binärzahl verbundene Liste kann zur Bestimmung der Parität verwendet werden.

# Beispiel:
#       repo_binary_number = RepoBinaryNumber()
#       repo_binary_number.add(binary_number1)
#       repo_binary_number.add(binary_number2)
#       print(repo_binary_number.sum_all())
