"""
a.Skriv ett program som anropar en funktion från en funktion.

Funktionen ska behandla en parameter som i detta fall är ett flytande tal. 
Talet ska i den första funktionen som anropats halveras och sedan skickas in i den andra funktionen där talet ska dubbleras. 
Därefter ska det dubblerade talet returneras till där första funktionen anropades och skrivas ut.
"""

def f1(f):
    f /= 2
    return f2(f)

def f2(f):
    return f*2

print(f1(float(input("Skriv in en float: "))))