#auteur marien manima-----

try:

    print("Saisir le valeur entier !!!")

    x=int(input("Saisir  la valeur de X\n"))
    b=str(format(int(input("Saisir la valeur de l'exposant \n")),'0b'))
    n=int(input("Saisir la valeur de N\n"))

    type=[]

    #calcul

    for i in range(len(b)):
        if(i==0):
            type.append([0,2,0,n,x])
        else:
            if(b[i]=="1"):
                type.append([type[i-1][4],2,x,n,((type[i-1][4]**2)*x)%n])
            else:
                type.append([type[i - 1][4], 2, 0, n, (type[i - 1][4] ** 2) % n])



    #affichage
    for i in range(len(type)):
        if(i!=0):
            if(type[i][2]==0):
                print(type[i][0],"**",2,"x(mod",n,")=",type[i][4])
            else:
                print(type[i][0], "**", 2,"x(",x, "mod", n, ")=", type[i][4])
        else:
            print(x)


    print("les valeurs sont  :",type[len(type)-1][4])
except:
    print("vous avez mal saisi les données !!!")
    print("vous êtes obligé de recommencer !!!!")