#password_generator.py
#Date: 27/September/2020
#by irving-rs

#Description:
#Password Generator: A simple, yet useful, aleatory password generator.

#Details:
#This password generator includes the following elements:
#Capital letters.
#Small letters.
#Numbers.
#Basic signs and symbols.

#Modules:
from random import randrange

#Functions:
def password(): #Generates password. Returns a string with the password.
    list_1 = []
    list_2 = []
    paswd = ""
    #Capital letters:
    for i in range(upl):
        x = randrange(len(uppercase)) #Aleatory generation.
        list_1.append(uppercase[x]) #Capital letter storage.
    #Small letters:
    for i in range(lwl):
        x = randrange(len(lowercase)) #Aleatory generation.
        list_1.append(lowercase[x]) #Small letter storage.
    #Numbers:
    for i in range(num):
        x = randrange(10) #Aleatory generation.
        list_1.append(str(x)) #Number storage.
    #Symbols and signs:
    for i in range(sym):
        x = randrange(len(symbols)) #Aleatory generation.
        list_1.append(symbols[x]) #Number storage.
    #Mixing the position of aleatory generated numbers:
    for i in range(len(list_1)):
        x = randrange(len(list_1)) #Mixing.
        list_2.append(list_1[x]) #Rearranging.
        del list_1[x]
    paswd = paswd.join(list_2) #Convertion from list to string.
    return paswd

def verify_input(): #Verifies the input. Returns True if correct, and False if wrong.
    suma = upl + lwl + num + sym #Counts the number of digits.
    if suma < 8: #If the number of digits do not reach 8.
        print("\nPassword must contain at least 8 digits. Try again...\n")
        return False
    elif upl<1 or lwl<1 or num<1 or sym<1: #If does not contain a digit of a certain element.
        print("\nPassword must contain at least 1 digit of each element. Try again...\n")
        return False
    else: #If the input is correct.
        return True


#Variables:
escape = False


#Construction of variables (using ASCII table):
uppercase = [chr(i) for i in range(65,91)]
lowercase = [chr(i) for i in range(97,123)]
symbols = [chr(i) for i in range (33,48)]
for i in range(58,65):
    symbols.append(chr(i))
for i in range(91,97):
    symbols.append(chr(i))
for i in range(123,127):
    symbols.append(chr(i))
    

#Presentation:
print("\nPassword Generator:\n")


#Instructions:
print("Instructions:")
print("1. Password must contain at least 8 digits.")
print("2. Password must contain at least 1 digit of the following elements:")
print("   a) Capital letters   b) Small letters   c) Numbers   d)Basic signs and symbols\n")


#Main body:
while escape == False:
    upl = int(input("a) Capital letters: "))
    lwl = int(input("b) Small letters: "))
    num = int(input("c) Numbers: "))
    sym = int(input("d) Basic signs and symbols: "))
    escape = verify_input()
    
paswd = password() #Generates the password.

print("\nThe resulting password is:", paswd, "\n")
