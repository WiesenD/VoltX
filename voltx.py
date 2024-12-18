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
        
        try:
            Ri = int(Ri)
            if Ri <= 0:
                print("Bitte eine Zahl grösser 0 eingeben.")
                continue
            R.append(int(Ri))
        
        except ValueError:
            print("Bitte eine Zahl eingeben.")
        
        i+=1
                
    if R:
        Rtot = 1 / sum(1/r for r in R)
        print("\n")
        print("Die Widerstaende waren: ",R)
        print("Rtot =", Rtot)
        print("\n")
    else:
        print("Keine Widerstände eingegeben.\n\n")
        
    wait()
    
# Funktion für Serie Schaltungen
def serie_widerstaende():
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
        Rtot = sum(r for r in R)
        print("\n")
        print("Die Widerstände waren: ",R)
        print("Rtot =", Rtot)
        print("\n")
    else:
        print("Keine Widerstaende eingegeben.\n\n")
        
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
    
# Funktion für die Lineare Widerstandsveränderung
def lin_RT():
    initialize()
    
    R20_string = input("Widerstand bei 20° eingeben: ")
    RT_string = input("Widerstand bei T eingeben: ")
    T2_string = input("Endtemperatur eingeben: ")
    TCR_string = input("Temperatur Koeffizient eingeben: ")
    T1 = 20
    
    if R20_string == '':
        case = 1
    elif RT_string == '':
        case = 2
    elif T2_string == '':
        case = 3
    elif TCR_string == '':
        case = 4
        
    R20 = float(R20_string) if R20_string else None
    RT = float(RT_string) if RT_string else None
    T2 = float(T2_string) if T2_string else None
    TCR = float(TCR_string) if TCR_string else None
    
    print("\n")
    if case == 1:
        R20 = RT/(1+TCR*(T2-T1))
        print(f"Widerstand bei 20° = {R20}")
    elif case == 2:
        RT = R20*(1+TCR*(T2-T1))
        print(f"Widerstand bei {T2} = {RT}")
    elif case == 3:
        T2 = T1+(RT/R20-1)/TCR
        print(f"Endtemperatur ist = {T2}")
    elif case == 4:
        print("Ausgabe von Temperatur Koeffizient nicht moeglich.")
    else:
        print("Alle Werte bereits vorhanden.")
    
    print("\n")                
    wait()
    
# Funktion für die Exponentielle Widerstandsveränderung
def exp_RT():
    initialize()
    
    R20_string = input("Widerstand bei 20° eingeben: ")
    RT_string = input("Widerstand bei T eingeben: ")
    T2_string = input("Endtemperatur eingeben: ")
    TCRa_string = input("Temperatur Koeffizient alpha eingeben: ")
    TCRb_string = input("Temperatur Koeffizient beta eingeben: ")
    T1 = 20
    
    if R20_string == '':
        case = 1
    elif RT_string == '':
        case = 2
    elif T2_string == '':
        case = 3
    elif TCRa_string == '' or TCRb_string == '':
        case = 4        
   
    R20 = float(R20_string) if R20_string else None
    RT = float(RT_string) if RT_string else None
    T2 = float(T2_string) if T2_string else None
    TCRa = float(TCRa_string) if TCRa_string else None
    TCRb = float(TCRb_string) if TCRb_string else None
    
    print("\n")
    if case == 1:
        R20 = RT/(1+TCRa*(T2-T1)+TCRb*(T2-T1)**2)
        print(f"Widerstand bei 20° = {R20}")
     
    elif case == 2:
        RT = R20*(1+TCRa*(T2-T1)+TCRb*(T2-T1)**2)
        print(f"Widerstand bei {T2} = {RT}")
        
    elif case == 3:
        # Mitternachtsformel
        a = TCRb
        b = TCRa-2*TCRb*T1
        c = 1 + TCRa * T1+ TCRb * T1**2 - RT / R20
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            T2_1 = (-b * np.sqrt(discriminant)) / (2*a)
            T2_2 = (-b * np.sqrt(discriminant)) / (2*a)
            print(f"Mögliche Temperaturen: T2_1 = {T2_1}, T2_2 = {T2_2}")
        else:
            print("Keine reelle Lösung für T2.")
    
    elif case == 4:
        print("Ausgabe von Temperatur Koeffizient nicht moeglich.")
        
    else:
        print("Alle Werte bereits vorhanden.")
    
    print("\n")
    wait()
      
# Funktion zur Menü-Darstellung
def print_menu():
    print("Was willst du machen?")
    for key, value in funktionen.items():
        print(f"{key}. {value.__name__}")

# "Menü" 
funktionen = {
    0: beenden,
    1: parallele_widerstaende,
    2: serie_widerstaende,
    3: dreieck_zu_stern,
    4: stern_zu_dreieck,
    5: lin_RT,
    6: exp_RT,
}

# Auswahl der Menüpunkte
initialize()
while True:
    print_menu()
    
    auswahl = int(input("Programm Auswaehlen:\n\n"))
    if auswahl == 0:
        cls()
        break
    else:
        try:
            funktionen[auswahl]()
        
        # Fehlerbehandlung
        except KeyError:
            print("\nUngueltige Auswahl.\n")
        except ValueError:
            print("\nBitte eine Zahl eingeben.\n")
        except Exception:
            print("\nError 404\n")
    