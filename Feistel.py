
def convertir_chaine(nombre):
    return str(nombre)


def convertir_entier(chaine):
    return int(chaine) 
     
def renverser_chaine(chaine):
     return chaine[::-1]   
 
def decalage(decals,x,ordre):
    
    decal = convertir_entier(decals)
    ordre_converti =convertir_entier(ordre)
    if len(x) >= ordre_converti:
        L = ""
        L1 = ""
        R = ""
        R1 = ""
        if decal == 1 :
            for i in range(ordre_converti):
                L += x[i]
            for j in range(ordre_converti,len(x)) :
                   L1 += x[j]
            return L1+L       
        elif decal == 2:
              D = len(x)
              for i in range(ordre_converti):
                  D -= 1
                  R += x[D]
              R2 = renverser_chaine(R)
              for j in range(len(x) - ordre_converti) :
                  R1 += x[j] 
              
              return R2+R1
                  
        else:
            print("il faut les choses qu'on te dit")    
    else:
        print("impossible de faire le decalage")    
 
    
def diviseur(x):
    taille_x = len(x)  
    M = ""
    N = ""
    T = []
    D = taille_x / 2
    for i in range(taille_x):
         if i < D :
          M += x[i]   
         else:
          N += x[i]
    T.append(M)
    T.append(N)      
    return T
    
          
def ou_exclusif(a,b):
    if len(a) == len(b):
       ou_exclusif = ""
       for i in range(len(a)):
           if a[i] == b[i] :
               ou_exclusif += "0"
           else:
               ou_exclusif += "1"    
       return ou_exclusif 
    else:
        print("impossible de faire le ou exclusif car la taille de valeur sont differentes")    


def ou_inclusif(a,b):
    if len(a) == len(b):
       ou_inclusif = ""
       for i in range(len(a)):
           if a[i] == "0" and b[i] == "0" :
               ou_inclusif += "0"
           else:
               ou_inclusif += "1"    
       return ou_inclusif 
    else:
        print("impossible de faire le ou inclusif car la taille de valeur sont differentes")    


def ET_logique(a,b):
    if len(a) == len(b):
       ou_inclusif = ""
       for i in range(len(a)):
           if a[i] == "1" and b[i] == "1" :
               ou_inclusif += "1"
           else:
               ou_inclusif += "0"    
       return ou_inclusif 
    else:
        print("impossible de faire le ET logique car la taille de valeur sont differentes")    


def inverse_permutation(G):
    W = ""
    for i in range(len(G)):
        for j in range(len(G)):
           if i == convertir_entier(G[j]):
              W += convertir_chaine(j)
              
    return W         
            

def permutation(x,y):
    x_convertis = x
    y_convertis = y
    taille_x = len(x_convertis)
    taille_y = len(y_convertis)
    if taille_x == taille_y :
        permuter =""
        for i in range(taille_x):
            rang = convertir_entier(y_convertis[i])
            permuter += x_convertis[rang]
        
        return permuter     
    else:
       print("impossible de permuter car la taille de x est différent de celui de y")    
 




print("********* le corps du programme ***********")
print()
print("Algorithme pour la génération des clés : ")
print()
longueur_cle = int(input("Saisir la taille du K : "))
v = True
while v:
    valeur_k = input("Saisir la valeur du K : ")
    if len(valeur_k) == longueur_cle:
        v = False
    else:
        print("La longueur de la valeur de K n'est pas correcte !!  vérifier si sa taille correspond a la taille entrée!!!!")
c = True
while c:
    fonction_permutation = input("Saisir la fonction de permutation de la clé : ")
    if len(fonction_permutation) == longueur_cle:
        c = False
    else:
        print("La longueur de K est différente de celle de la fonction de permutation !!")

print("Saisir le décalage pour K1. G ou D")
d = True

while d:
    decalage_input = input()
    delta = decalage_input.upper()
    if delta == "G":
        ordre_Dk1 = int(input("Saisir l'ordre du décalage : "))
        d = False
        decalk1 = 1
    elif delta == "D":
        ordre_Dk1 = int(input("Saisir l'ordre du décalage : "))
        d = False
        decalk1 = 2
    else:
        print("Saisir G ou D")

print("Saisir le décalage pour K2. G ou D")
d = True

while d:
    decalage_input = input()
    delta = decalage_input.upper()
    if delta == "G":
        ordre_Dk2 = int(input("Saisir l'ordre du décalage : "))
        d = False
        decalk2 = 1
    elif delta == "D":
        ordre_Dk2 = int(input("Saisir l'ordre du décalage : "))
        d = False
        decalk2 = 2
    else:
        print("Saisir G ou D")

p = permutation(valeur_k, fonction_permutation)
l = diviseur(p)

kd1 = l[0]
kd2 = l[1]

kn1 = ou_exclusif(kd1, kd2)
kn2 = ET_logique(kd1, kd2)

k1 = decalage(decalk1,kn1, ordre_Dk1)
k2 = decalage(decalk2,kn2, ordre_Dk2)

print("*** Algorithme de chiffrement ***")
print()
v = True
while v:
    valeur_N = input("Saisir la valeur du N : ")
    if len(valeur_N) == longueur_cle:
        v = False
    else:
        print("La longueur de la valeur de not n'est pas correcte. vérifier si sa taille correspond a la taille entrée  !!")
c = True
while c:
    fonction_permutation_N = input("Saisir la fonction de permutation de N : ")
    if len(fonction_permutation_N) == longueur_cle:
        c = False
    else:
        print("La longueur de N est différente de celle de la fonction de permutation !!")
        
P = permutation(valeur_N,fonction_permutation_N)       
 
D = diviseur(P)
G0 = D[0]
D0 = D[1]

D1 = ou_exclusif(permutation(G0,"2013"),k1)
G1 = ou_exclusif(D0,ou_inclusif(G0,k1))

D2 = ou_exclusif(permutation(G1,"2013"),k2)
G2 = ou_exclusif(D1,ou_inclusif(G1,k2))

C1 = G2 + D2 
inverse = inverse_permutation(fonction_permutation_N)
C = permutation(C1,inverse)
print()
print("le mot chiffrer est ",C)
print()

print("*** Algorithme de déchiffrement ***")
print()
v = True
while v:
    valeur_Nd = input("Saisir la valeur du N chiffrer : ")
    if len(valeur_Nd) == longueur_cle:
        v = False
    else:
        print("La longueur de la valeur de N n'est pas correcte. vérifier si sa taille correspond a la taille entrée  !!")

P1 = permutation(valeur_Nd,fonction_permutation_N) 


Dd = diviseur(P1)
Gd2 = D[0]
Dd2 = D[1]

inv = inverse_permutation("2013")
Gd1 = permutation(ou_exclusif(Dd2,k2),inv)
Dd1 = ou_exclusif(Gd2,ou_inclusif(Gd1,k2))

Gd0 = permutation(ou_exclusif(Dd1,k1),inv)
Dd0 = ou_exclusif(Gd1,ou_inclusif(Gd0,k1))

C2 = Gd0 + Dd0
C = permutation(C2, inverse)

print("le mot déchiffrer est  ",C)

