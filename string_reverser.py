""" 
4.Skriv ett program som vänder på en strängsom användaren skriver in. 
”Hej” blir ”jeH”.

Funktionen ska ha en parameter som i detta fall är användarens inmatning.
"""

def string_reverser(s):
    return s[::-1]

user_input = input("Skriv in en sträng: ")

print(string_reverser(user_input))