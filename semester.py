"""
2.Jag semestrar i USA men hänger inte med deras enhetssystem.
Skapa ett program som hjälper mig omvandla från Fahrenheit till Celsius.
Lägg till en funktion som omvandlar från pounds (lb)till kg.
Lägg till en funktion som omvandlar feet till meter.

Celsius=5/9 * (Fahrenheit-32)
1 kg = 2.2 lbs
1 m = 3.3 foot2
"""

def FarToCel(fahrenheit):
    return (5/9 * (fahrenheit-32))

def LbsToKg(lbs):
    return lbs/2.2

def FtToM(ft):
    return ft/3.3

def main():
    print("Farenheit to Celsius:",FarToCel(100))
    print("LBS to KG:",LbsToKg(220))
    print("FT to M:",FtToM(330))
    
if __name__ == "__main__":
    main()