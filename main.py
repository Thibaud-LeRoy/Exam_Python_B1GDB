##-----------LIBRAIRIES-----------##
from colorama import init
init()
from colorama import Fore, Back, Style
import random
##-------------------------------##

#Génération aléatoire du mot
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

#Cherche une lettre dans un mot
def chercheLettre(lettreTest,motChoisi):
    print(motChoisi)
    for i in range(0,len(motChoisi)):
        if(lettreTest==motChoisi[i]):
            print("il y a bien cette lettre dans le mot")
            print(i)
            input()
        else:
            print("il n'y a pas cette lettre dans le mot")


#Comparaison des deux mots et application des couleurs sur les lettres
def compareMot(nouveauMot,motChoisi):
    compteur = 0 
    for compteur in(0,longueurMot):
        #--------------------------------------------SI LES LETTRES SONT BIEN PLACÉES
        if(nouveauMot[0]==motChoisi[0]):
            print(Style.RESET_ALL)
            print(Back.RED + nouveauMot[0],end="")
            
        if(nouveauMot[1]==motChoisi[1]):
            print(Style.RESET_ALL)
            print(Back.RED + nouveauMot[1],end="")
            
        if(nouveauMot[2]==motChoisi[2]):
            print(Style.RESET_ALL)
            print(Back.RED + nouveauMot[2],end="")
            
        if(nouveauMot[3]==motChoisi[3]):
            print(Style.RESET_ALL)
            print(Back.RED + nouveauMot[3],end="")
            
        if(nouveauMot[4]==motChoisi[4]):
            print(Style.RESET_ALL)
            print(Back.RED + nouveauMot[4],end="")
            
        if(nouveauMot[5]==motChoisi[5]):
            print(Style.RESET_ALL)
            print(Back.RED + nouveauMot[5])
       
        if(nouveauMot[0]==motChoisi[0] and nouveauMot[1]==motChoisi[1] and nouveauMot[2]==motChoisi[2] and nouveauMot[3]==motChoisi[3] and nouveauMot[4]==motChoisi[4] and nouveauMot[5]==motChoisi[5]):
            motTrouve = True
        #-------------------------------------------SI LES LETTRES NE SONT PAS BIEN PLACÉES
        if(nouveauMot[0]==motChoisi[1] or nouveauMot[0]==motChoisi[2] or nouveauMot[0]==motChoisi[3] or nouveauMot[0]==motChoisi[4] or nouveauMot[0]==motChoisi[5]):
            print(Style.RESET_ALL)
            print(Back.YELLOW + nouveauMot[0],end="")
            
        if(nouveauMot[1]==motChoisi[0] or nouveauMot[1]==motChoisi[2] or nouveauMot[1]==motChoisi[3] or nouveauMot[1]==motChoisi[4] or nouveauMot[1]==motChoisi[5]):
            print(Style.RESET_ALL)
            print(Back.YELLOW + nouveauMot[0],end="")
            
        if(nouveauMot[2]==motChoisi[0] or nouveauMot[2]==motChoisi[1] or nouveauMot[2]==motChoisi[3] or nouveauMot[2]==motChoisi[4] or nouveauMot[2]==motChoisi[5]):
            print(Style.RESET_ALL)
            print(Back.YELLOW + nouveauMot[0],end="")
            
        if(nouveauMot[3]==motChoisi[0] or nouveauMot[3]==motChoisi[1] or nouveauMot[3]==motChoisi[2] or nouveauMot[3]==motChoisi[4] or nouveauMot[3]==motChoisi[5]):
            print(Style.RESET_ALL)
            print(Back.YELLOW + nouveauMot[0],end="")
            
        if(nouveauMot[4]==motChoisi[0] or nouveauMot[4]==motChoisi[1] or nouveauMot[4]==motChoisi[2] or nouveauMot[4]==motChoisi[3] or nouveauMot[4]==motChoisi[5]):
            print(Style.RESET_ALL)
            print(Back.YELLOW + nouveauMot[0],end="")
        
        if(nouveauMot[5]==motChoisi[1] or nouveauMot[5]==motChoisi[2] or nouveauMot[5]==motChoisi[3] or nouveauMot[5]==motChoisi[4] or nouveauMot[5]==motChoisi[0]):
            print(Style.RESET_ALL)
            print(Back.YELLOW + nouveauMot[0])
       
        #-------------------------------------------SI LES LETTRES NE SONT PAS DANS LE MOT
        if(nouveauMot[0]!=motChoisi[0]):
            print(Style.RESET_ALL)
            print(Back.BLUE + nouveauMot[0],end="")
        if(nouveauMot[1]!=motChoisi[1]):
            print(Style.RESET_ALL)
            print(Back.BLUE + nouveauMot[1],end="")
        if(nouveauMot[2]!=motChoisi[2]):
            print(Style.RESET_ALL)
            print(Back.BLUE + nouveauMot[2],end="")
        if(nouveauMot[3]!=motChoisi[3]):
            print(Style.RESET_ALL)
            print(Back.BLUE + nouveauMot[3],end="")
        if(nouveauMot[4]!=motChoisi[4]):
            print(Style.RESET_ALL)
            print(Back.BLUE + nouveauMot[4],end="")
        if(nouveauMot[5]!=motChoisi[5]):
            print(Style.RESET_ALL)
            print(Back.BLUE + nouveauMot[5])
    return()

#On demande 6 lettres à l'utilisateur et on les inscrits dans un tableau de chaine de caractères
def nouveau_Mot_User(nouveauMot):
    for i in range (0,longueurMot):
        print(Style.RESET_ALL)
        lettre =input("lettre ?")
        nouveauMot += lettre
        print(nouveauMot)
    

motTrouve = False
motChoisi=["","","","","",""]
nouveauMot = []
longueurMot = len(motChoisi)
lettreTest="e"
#Liste des 10 mots intègres au jeu
mot0 = ["t","o","m","a","t","e"]
mot1 = ["b","a","n","a","n","e"]
mot2 = ["v","e","l","o","t","s"]
mot3 = ["m","a","r","m","o","t"]
mot4 = ["f","e","s","t","i","f"]
mot5 = ["u","l","t","i","m","e"]
mot6=  ["p","r","i","s","m","e"]
mot7 = ["v","i","t","a","u","x"]
mot8 = ["d","u","r","i","o","n"]
mot9 = ["m","a","s","s","e","r"]



motChoisi = choisirMot()
print(motChoisi)#affiche le mot généré aléatoirement


#chercheLettre(lettreTest,motChoisi)


essai = 0 
while(essai <= 8 and motTrouve==False):
    nouveau_Mot_User(nouveauMot)
    compareMot(nouveauMot,motChoisi)
    essai= essai+1
    if(essai==8):
        print("C'est perdu ! D:")
        input()
    if(motTrouve==True):
        print("c'est gagné ! :D")
        input()
