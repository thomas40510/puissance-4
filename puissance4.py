import numpy as np


#génération de la grille de jeu
plateau = []
plateau.append(["/"," " ,"A","B","C","D","E","F","G"])
for i in range(6):
    plateau.append([i+1,"|",".",".",".",".",".",".","."])
    
# Affichage d'une matrice 
def Affiche(M):
    nligne=len(M)
    ncolonne=len(M[0])
    for i in range(0,nligne):
        for j in range(0,ncolonne) :
            print(M[i][j],end=' ')
        print()


Affiche(plateau)
      
#c'est au joueur de jouer
def playerTurn():
    p = input("Où voulez-vous jouer ? ")
    a = plateau[0].index(p[0])
    print("indice", plateau[0].index(p[0]))
    n = 0
    print(p[1])
    try :
        while(int(p[1])!=plateau[n][0]):
            n+=1
        plateau[n][a] = "X"
    except IndexError:
        print("erreur d'index")
        playerTurn()
playerTurn()

Affiche(plateau)

