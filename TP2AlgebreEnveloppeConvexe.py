# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt, pi, log, cos, sin, exp
from matplotlib.pyplot  import *
## from imtools import *
import matplotlib.gridspec as gridspec
import os


os.system("cls")
"""
Created on Wed Jan 31 16:35:33 2018

TP2 Algebre : envelopppe convexe- Marche de Jarvis, Diagramme de Voronoï-Algorithme de Green et Sibson

@author: Claire
"""


33##########################################################"
############ Enveloppe convexe-Marche de Jarvis ####################
############################################################"


def norme(P,Q):
    return sqrt(float((Q[0]-P[0])**2+ (Q[1]-P[1])**2))

x=norme([1,1],[0,0])
print(x)

def vec(A,B):
    return [B[0]-A[0],B[1]-A[1]]
def COS(A,B,C):
    x=float(vec(A,B)[0]* vec(A,C)[0]+vec(A,B)[1]* vec(A,C)[1])/(norme(A,B)*norme(A,C))
    return x
    
def SIN(A,B,C):
    x=float(vec(A,B)[0]* vec(A,C)[1]- vec(A,B)[1]* vec(A,C)[0])/(norme(A,B)*norme(A,C))
    return x
    
A=[0,0]
B=[2,0]
E=[0,2]
C=[1,1]
D=[-1,-1]
print(sin(pi/4.))
print(SIN(A,B,C))
print(SIN(A,B,D))
print(SIN(A,D,B))

print(COS(A,B,C))
print(COS(A,B,E))

  ###on définit une fonction qui donne le point de la famille de points P 
#le plus à droite de  la demi-droite [A,B)   
def LePlusADroite(A,B,P):
     m=1
     Q=[]
     
     for X in P: 
         if (X!=A) and (X!=B):
             t=COS(A,B,X)
             if t<m: 
                 Q=[X]
                 m=t
                 #print(Q)
             elif t==m:
               Q.append(X)
                #print(Q)
     if len(Q)== 1:
        return Q[0]
     else: 
        d=0
        M=Q[0]
        for X in Q:
            u=norme(A,X)
            if u>d :
                M=X
                d=u
     return M
    
    
def ordonneminimale(P):
    
    y=P[0][1]
    x=P[0][0]
    j=0
 
    for k in range(len(P)):
        if P[k][1]<y:
            y=P[k][1]
            x=y=P[k][0]
            j=k
            
        elif P[k][1]==y:
            if P[k][0]<x:
                x=P[k][0]
                j=k
    return j
     
           
                
    
def MarcheJarvis(P):
    L=[P[0]]
    A=[P[0][0],P[0][1]] ### initialisation de A  au point d'ordonnée minimale 
    M=[P[0][0]+1,P[0][1]] #### point courant
    while (M != P[0]):
        B=LePlusADroite(M,A,P)
        A=M
        M=B
        print('A,M',A,M)
     #plot([A[0],M[0]],[A[1],M[1]])
        L.append(M)
    
    return L
    
    
#P=[[0,0], [2,2],[1,3],[1,2], [-1,1]]
P=[[0,0],[0,3],[3,0], [2,2],[1,3],[0.5,2],[1,5],[-5,4], [-1,1]]

print('1',COS([2,2],[1,3],[-1,1]))
print('2',COS([2,2],[1,3],[1,2]))

axis('scaled')
axis([-6,6,-6,6])
T=MarcheJarvis(P)
#plot([0,0],'*') 
#plot([2,2],'o')
      
for j in range(len(P)):
    #print(P[j])
    plot([P[j][0]],[P[j][1]],'o')

    
    
#U=[T[j][0] for j in range(len(P))]
#U.append(T[0][0])
#V=[T[j][1] for j in range(len(P))] 
#V.append(P[0][1])
#plot(U,V)
    
print( 'Le plus a droite', LePlusADroite([2,2],[1,3],P))
    
X=[T[j][0] for j in range(len(T))]
X.append(T[0][0])
Y=[T[j][1] for j in range(len(T))]
Y.append(T[0][0])
print('T=',T)
plot(X,Y)
     
        
        
                #############################################
         ############  Diagramme Voronoï  ####################
             #########################################
             
    
