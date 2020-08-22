#Defines the main code
def rechner():
    aufgabe = input('''
Willkommen im Rechner :-)

Bitte geben den Matematischen Operator an den du Benutzen willst:
+ für Addition
- für Subtraktion
* für Multiplikation
/ für Teilung
''')

# Print the Posiblities for the calculator


    nummer_1 = int(input("Erste Zahl"))
    nummer_2 = int(input("Zweite Zahl"))

    #Addition
    if aufgabe == "+":
        print('{} + {} = '.format(nummer_1, nummer_2))
        print(nummer_1 + nummer_2)

    #Subtraction
    elif aufgabe == "-":
        print('{} - {} = '.format(nummer_1, nummer_2))
        print(nummer_1 - nummer_2)

    #Multiplication
    elif aufgabe == "*":
        print('{} * {} = '.format(nummer_1, nummer_2))
        print(nummer_1 * nummer_2)


    #Division
    elif aufgabe =="/":
        print('{} / {} = '.format(nummer_1, nummer_2))
        print(nummer_1 / nummer_2)


    else:
        print("Ungültiger Operator, bitte lade das Programm neu")
 #Calls rechner() outside of the function
    wieder()

#Defines the end of the code 
def wieder():

    # List the Possibility
    rech_wieder = input('''
Willst Du wieder etwas rechnen ?
Bitte schreibe y für ja oder n für Nein.
ps. muss Kleingeschrieben sein
''')
    #Possibility Jes
    if rech_wieder == "y":
        rechner()

    #Possibility No
    if rech_wieder == "n":
        print("Bis später :-)")

    #Different option basically calls the main programm
    else:
        wieder()

rechner()
    
