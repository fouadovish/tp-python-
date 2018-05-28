
# coding: utf-8

# In[1]:


#les étudiants ayant contribué à cette feuille de calcul: MEHIRI ElMehdi 201500010214, SAIDI Fouad 201500008229, BACHA Bouchra 201500009076, KECHIR Mellila 201500009129
from math import sqrt

a=input("donner un nbr a \n")
a=int(a)
b=input("donner un nbr b\n")
b=int(b)
# In[2]:


# nbre_prem est une fonction qui nous liste les nombres premiers compris entre les deux entiers a et b

def nbre_prem(a,b):
	p = []

	for i in range( max(a,2) , b):
		for j in range(2, int(sqrt(i))+1 ) :
			if i%j == 0 :
				break
		else :
			p.append(i)
	return set(p)


# In[3]:


# liste_comb est une fonction qui nous liste toutes le combinaisons possibles des nombres entre deux entiers a et b

def liste_comb(a) :
	comb = [ [] ]
	
	for i in a :
		for sous_ens in comb :
			comb = comb + [list(sous_ens)+[i]]
	
	return comb[1:]


# In[4]:


def C(a, b):
	if type(a) != int or type(b) != int :
		print("Donner les bornes entières positives a et b")
		return

	if a > b or min(a, b) < 0 :
		print("Les bornes données sont invalides")
		return

	intervalle = set( range(a, b+1) )
	
	# supression des nombres premiers
	if b > 2*a :
		intervalle = intervalle - nbre_prem(2*a, b)

	else :
		p = nbre_prem(b-a, a)

		for i in p :
			if b//i != i :
				intervalle = intervalle - set( [(b//i)*i] )

		intervalle = intervalle - nbre_prem(a+1, b+1)

	intervalle = list(intervalle)
	sous_ensemble = liste_comb(intervalle)

	#test des sous ensembles
	s = 0
	
	for i in sous_ensemble :
		m = 1

		for j in i :
			m = m*j

		if sqrt(m)%1 == 0 :
			s = s + 1

	print( " Le nombre de sous-ensembles non vides  dans lesquels le produit de tous les éléments est un carré parfait entre",(a, b) ,"=", s )


# In[5]:


C(a,b)

