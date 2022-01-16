#memoire MCMC - Propp-Wilson
#Adly Zaroui M1IM

import numpy as np

#E={1,2,3}
#P=np.array([[0.1,0.3,0.6],[0.4,0.3,0.3],[0.5,0.15,0.35]])
#F(E,P,i,x) renverra la fonction de repartition de la ligne i, evaluée en x

def F(E,P,i,x): #fonction de repartition de (P_i,j)_{j \in E} evaluée en x

	s=0
	for j in range(len(E)):
		if x>=j:
			s=s+P[i][j]
	return s


def fromPtoPhi(E,P,i,u): #fonction phi de mise à jour associée à P, evaluée en (i,u)

	s=0
	for j in range(len(E)):
		if F(E,P,i,j-1)<u and u<=F(E,P,i,j):
			s=s+j
	return s
#fromPtoPhi(E,P,i,u) renverra phi(i,u)



def etat_final(p,k,phi,U,N): #etat à l'instant 0 de (X_{t}^{(p,k)})_{-N_{p}<=t<=0}

	n = -N[p-1]
	i = 1
	while n < 0:
		k = phi(k,U[-i])
		n = n+1
		i=i+1
	return k

def PW(E,phi): #algorithme de Propp-Wilson

	U = np.random.random_sample((1,))
	N = [1]
	etats_finaux = [1,2]

	p=1
	while not all(e == etats_finaux[0] for e in etats_finaux): #tant que tous les etats finaux sont differents
		etats_finaux = []
		for k in E :
			etats_finaux.append(etat_final(p,k,phi,U,N))
		p=p+1
		U = np.append(U,np.random.random_sample((len(U),)))
		N.append(2*N[-1])
	return etats_finaux[0]
