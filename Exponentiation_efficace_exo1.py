
# coding: utf-8

# In[1]:


#les étudiants ayant contribué à cette feuille de calcul: MEHIRI ElMehdi 201500010214, SAIDI Fouad 201500008229, BACHA Bouchra 201500009076, KECHIR Mellila 201500009129
# Algorithme : Sliding Window, Refenrence : https://en.wikipedia.org/wiki/Exponentiation_by_squaring#Sliding_window_metho

def s_w(m, k):
    
    n = bin(m)  # conversion en binaire
    n = n[2:]   # supprimer le 1er élément du départ
    n = n[::-1] # on renverse la chaine de charactere pour faciliter son traitement

    # Precalcule : les puissances impaires
    
    x = { 1:2, 2:4 }
    
    for i in range(1, 2**(k-1) ) :
        x[2*i+1] = 2**(2*i+1)
    
    # nombre de multiplications effectuees jusqu'ici
    etape = len( range(1, 2**(k-1) ) ) + 1

    y, i = 1, len(n)-1
    max_utile = 0   # variable qui servira a enlever le coups des valeurs precalculee non utile du total

    while i > -1 :
        if n[i] == '0': 
            
            y = y**2
            i -= 1
            etape += 1
            
        else :
            # retrouve la chaine de longeur < k et qui se termine par 1 
            for j in range(k):
                lower = max(i-j,0)
                if n[lower] == '1':
                    d = int ( n[ lower : i+1], 2)
                    e = lower

            y = y**(2**(i-e+1))
            
            # compte le nombre de multiplication qui vient d'etre effectue
            if y > 1 :
                etape += i-e+1
            
            y = y*x[d]

            # max_utile reçoit le plus grand index utilise jusqu'ici
            max_utile = max(d, max_utile)
            i = e-1

            # ne compte pas la multiplication si c'est fois 1
            if y > x[ d ] :
                etape += 1
    
    # on soustrait au coups le nombre des elements precalculer non utile
    non_utile = [ 1 for i in x.keys() if i > max_utile ]
    etape -= sum(non_utile)

    return etape


# minProd() est un simple wrap de la fonction précedente afin de l'executer sur l'interval (0, k+1)


# In[2]:


def sommeminProd(k):
    
    somme = 0  # initialisation de la somme
    
    for a in range(2, k+1) :
        max_window = len( bin(a) )-2        # longeur de maximal de la fenetre = longueur de a en binaire
        etapes = [ s_w(a, b) for b in range(1, max_window ) ]
        somme += min( etapes )
        
    print( "Le nombre de multiplications necessaires à l'exponentiation pour n à la puissance de", k,": minprod =", min(etapes) )
    print( "Sommes du nombre de multiplications necessaires à l'exponenetiation pour chauque n de ( 1 à", k,") =", somme )


# In[3]:
a=input("donner un nbr\n ")
a=int(a)

sommeminProd(k=a)




