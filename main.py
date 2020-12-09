from colorama import init
init()
from colorama import Fore, Back, Style
import random

def choisirMot():
    cle = random.randint(0,9)
    if(cle==0):
        motChoisi = mot0
    if(cle==1):
        motChoisi = mot1
    if(cle==2):
        motChoisi = mot2
    if(cle==3):
        motChoisi = mot3
    if(cle==4):
        motChoisi = mot4
    if(cle==5):
        motChoisi = mot5
    if(cle==6):
        motChoisi = mot6
    if(cle==7):
        motChoisi = mot7
    if(cle==8):
        motChoisi = mot8
    if(cle==9):
        motChoisi = mot9
    return(motChoisi)
        
        
        
mot0 = ["t","o","m","a","t","e"]
mot1 = ["b","a","n","a","n","e"]
mot2 = ["v","e","l","o","t","s"]
mot3 = ["m","a","r","m","o","t"]
mot4 = ["f","e","s","t","i","f"]
mot5 = ["u","l","t","i","m","e"]
mot6= ["p","r","i","s","m","e"]
mot7 = ["v","i","t","a","u","x"]
mot8 = ["d","u","r","i","o","n"]
mot9 = ["m","a","s","s","e","r"]
print(choisirMot())


essai = 0 
while(essai <= 8):
    essai= essai+1
    if(essai==8):
        print("perdu !")
        input()