# 3.Skriv ett program som summerar alla talen i en lista m.h.a. en funktion.Skapa en valfri lista med minst 10 st tal (heltal eller flytande tal spelar ingen roll).

def listAdder(lst):
    return sum([i for i in lst])

def main():
    lst = [i for i in range(1,11)]
    print("Lista:",lst)
    print("Funktion:",listAdder(lst))
    
if __name__ == "__main__":
    main()