def Nim():
    from random import randint
    import sys
    from functools import reduce
    tas = [randint(1, 5), randint(1, 2), randint(1, 3),randint(1, 2)]

    print("Bienvenue au NIM!!")
    joueur1=input("entrez le nom de 1er joueur \n")
    joueur2=input("entrez le nom de 2eme joueur \n")

    print("Les tas sont {}" .format(tas))

    joueur = joueur1
    i=0;
    i=int(i)
    j=0
    j=int(j)
    res=0
    res=int(res)
    e=0
    e=int(e)
    
    while True:
         i+=1
         print("le joueur ", joueur)
            
         tass = input("choisir un tas entre 1 et 4\n")
         tass = int(tass)
         while tass > 4:
             print("votre choix est incorrecte choisissez un autre tas entre 1 et 4")
             tass = input()
             tass = int(tass)
             if 0 < tass <= 4:
                 break
             else:
                 e=e+1
                 
             
         while tas[tass-1]==0  :
                print("votre choix est incorrecte choisissez un autre tas entre 1 et 4")
            
                tass = input("choisir un tas\n")
                tass = int(tass)
                if tas[tass-1]!=0  :
                   break
                else:
                    e=e+1
                    break
                
         deplacement = input("quel est votre deplacement,choisir entre [1,2,3]\n")
         deplacement = int(deplacement)    
         while  0 < deplacement  <= 3 and 0 < tass <= 4  and tas[tass-1]!=0:
            
            
                  if tas[tass-1]<deplacement:
                      tas[tass-1]=0
                      print("Les tas maintenant sont {}" .format(tas))
                      break
            
    
                  else:

                      tas[tass-1] =tas[tass-1] - deplacement
                      print("Les tas maintenant sont {}" .format(tas))
                      break
                 
           
         if  deplacement > 3 :
                print("reprendre  le nombre de deplacement est incorrecte")
                joueur=joueur2
           
                
                    
                
              
         if tas==[1,0,0,0] or tas==[0,1,0,0] or tas==[0,0,1,0] or tas==[0,0,0,1] :
                print(" le joueur ", joueur, "a gagné")
                res=1
                break
         elif tas == [0,0,0,0]:
                print(" le joueur ", joueur, "a perdu")    
                res=0
                break
         if joueur == joueur1:
                joueur = joueur2
         else:
                joueur = joueur1
                
    n=1
    score=0
    while n<(i+1)/2 and res==1:
       score=score+n*((10)**n )
       n=n+1
    print("le score de",joueur,"est",score)

    print("game over")
    rep =input("faire une autre partie?[1/0]\n")
    if rep == '1' :
        Nim()
    else :
        print("see you next time")
Nim()
