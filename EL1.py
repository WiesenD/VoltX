import numpy as np
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def wait():
    input()
    cls()
    
def initialize():
    cls()
    
def beenden():
    print("")

# Funktion für Parallele Schaltungen
def parallele_widerstaende():
    initialize()
    
    R=[]
    i=1
        
    while True:
        Ri = input(f"R{i} eingeben: ")
        if Ri == '':
            break
        R.append(int(Ri))
        i+=1
                
    if R:
        Rtot = 1 / sum(1/r for r in R)
        print("\n")
        print("Die Widerstände waren: ",R)
        print("Rtot =", Rtot)
        print("\n")
    else:
        print("Keine Widerstände eingegeben.\n\n")
        
    wait()

# Funktion für Dreieck -> Stern
def dreieck_zu_stern():
    initialize()
    
    Rab = float(input("Rab eingeben: "))
    Rac = float(input("Rac eingeben: "))
    Rbc = float(input("Rbc eingeben: "))
    Rs = Rab+Rac+Rbc
    
    Ra = (Rab*Rac)/Rs
    Rb = (Rab*Rbc)/Rs
    Rc = (Rac*Rbc)/Rs
    
    print("\n")
    print("Ra = ",Ra)
    print("Rb = ",Rb)
    print("Rc = ",Rc)
    print("Rs = ",Rs)
    print("\n")
    
    wait()

# Funktion für Stern -> Dreieck
def stern_zu_dreieck():
    initialize()
    
    Ra = float(input("Ra eingeben: "))
    Rb = float(input("Rb eingeben: "))
    Rc = float(input("Rc eingeben: "))
    Rs = Ra*Rb + Ra*Rc + Rb*Rc
    
    Rab = Rs/Rc
    Rac = Rs/Rb
    Rbc = Rs/Ra
    
    print("\n")
    print("Rab = ",Rab)
    print("Rac = ",Rac)
    print("Rbc = ",Rbc)
    print("Rs = ",Rs)
    print("\n")
    
    wait()

# Funktion zur Menü-Darstellung
def print_menu():
    print("Was willst du machen?")
    for key, value in funktionen.items():
        print(f"{key}. {value.__name__}")

# "Menü" 
funktionen = {
    1: parallele_widerstaende,
    2: dreieck_zu_stern,
    3: stern_zu_dreieck,
    0: beenden
}

# Auswahl der Menüpunkte
initialize()
while True:
    print_menu()
    
    auswahl = int(input("Programm Auswaehlen:\n\n"))
    try:
        if auswahl == 1:
            parallele_widerstaende ()
        elif auswahl == 2:
            dreieck_zu_stern ()
        elif auswahl == 3:
            stern_zu_dreieck ()
        elif auswahl == 0:
            cls()
            break
        else:
            print("\nUngültige Auswahl.\n")
    except:
        print("Bitte gib eine Zahl ein.")
    