import os
import re

answer = input("Skriv in det ordet som skall gissas: ")
ans_list = []
letter_list = []
pos_list = []
wrong = []
tries = 0

def hangman(i):
    if i == 10:
        print(" /----   ")
        print(" |   |   ")
        print(" |   o   ")
        print(" |  /|\  ")
        print(" |  / \  ")
        print(" |       ")
        print("/ \      ")
    if i == 9:
        print(" /----   ")
        print(" |   |   ")
        print(" |   o   ")
        print(" |  /|\  ")
        print(" |  /    ")
        print(" |       ")
        print("/ \      ")
    if i == 8:
        print(" /----   ")
        print(" |   |   ")
        print(" |   o   ")
        print(" |  /|\  ")
        print(" |       ")
        print(" |       ")
        print("/ \      ")
    if i == 7:
        print(" /----   ")
        print(" |   |   ")
        print(" |   o   ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("/ \      ")
    if i == 6:
        print(" /----   ")
        print(" |   |   ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("/ \      ")
    if i == 5:
        print(" /----   ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("/ \      ")
    if i == 4:
        print(" /--     ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("/ \      ")
    if i == 3:
        print("         ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("/ \      ")
    if i == 2:
        print("         ")
        print("         ")
        print("         ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("/ \      ")
    if i == 1:
        print("         ")
        print("         ")
        print("         ")
        print("         ")
        print("         ")
        print(" |       ")
        print("/ \      ")
for letter in answer:
    letter_list.append(letter)

for i in range(0,len(answer)):
    ans_list.append((i,answer[i]))
    
    
os.system('cls')


while tries < 10:
    s = ""

    for element in ans_list:
        if element in pos_list:
            s +=  element[1] + " "
        else:
            s += "_ "

    print("Tries left: ",10-tries)
    print("Already guessed: ",wrong)
    hangman(tries)
    print(s[:-1])
    
    guess = (input("Gissa: "))
    try:    
        if len(guess) > 1 or guess.isalpha() == False:
            print("ONLY ONE LETTER! TRY AGAIN")
            continue
    except:
        print("WRONG INPUT, TRY AGAIN!")
   
    pattern = re.compile(guess)

    for m in pattern.finditer(answer):
        if (m.start(),m.group()) not in pos_list:
            pos_list.append((m.start(),m.group()))
              
    if guess in letter_list:
        print("Match!")
    else:
        if guess not in wrong:
            print("Wrong!")
            wrong.append(guess)
            tries += 1
        else:
            pass
        
    if len(pos_list) == len(answer):
        break

if tries == 10: 
    os.system('cls')
    print("         /----   ")
    print("         |   |   ")
    print("         |   o   ")
    print("         |  /|\  ")
    print("         |  / \  ")
    print("         |       ")
    print("        / \     ")
    print()
    print("TOO BAD YOU LOSE! THANK YOU COME AGAIN!")
else:
    print("******************* YOU WIN! *********************")