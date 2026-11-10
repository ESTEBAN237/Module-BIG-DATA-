import random
def tri_bulle(liste):
    n = len(liste)
    print("Taille de la liste :", n)
    
    for i in range(n):
        # Les i derniers éléments sont déjà triés, pas besoin de les revérifier
        for j in range(0, n - i - 1):
            # Comparer les éléments adjacents
            if liste[j] > liste[j + 1]:
                # Intervertir les éléments si le premier est plus grand que le second
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                
    return liste

ma_liste = [5, 7, 10, 4, 8, 9, 1]
listeVide = []
liste3 = []
for i  in range (1000) : 
    liste3.append(random.randint(0,1000))   

L = sorted (liste3)
NewListe3 = tri_bulle(liste3)

for i in range (len(liste3)):
    if (NewListe3 [i] != L [i]):
        print ("pas bon")
    else :
        print ("It's Okay")