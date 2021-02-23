# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:43:19 2021

@author: Cristian
"""

print('Sistema de notas.')

#Entrada.

N=int(input('Ingrese la cantidad de estudiantes: '))
#Contadores.
z=list(range(N))
count=1
apr=0
rep=0
suma=0
aprobados=0
reprobados=0
maxi=0
mini=5
#Ciclo.
for i in z:
    #Nombre.
    n=input('Ingrese el nombre del estudiante: ')
    #Notas.
    n1=float(input('Ingrese la primera nota: '))
    n2=float(input('Ingrese la segunda nota: '))
    n3=float(input('Ingrese la tercera nota: '))
    #Definitiva.
    de=(n1+n2+n3)/3
    print('La definitiva de',n,' es: ',round(de,1))
    #Procesos.
    if de>=3.0:
        apr=apr+1
        aprobados=aprobados+de
    else:
        rep=rep+1
        reprobados=reprobados+de
    if de>maxi:
        maxi=de
    if de<mini:
        mini=de
    count=count+1
    suma=suma+de
pro=suma/N
#Entrega de resultados.
print('Cantidad de estudiantes aprobados es: ',apr)
print('Cantidad de estudiantes reprobados es: ',rep)
print('El promedio del grupo es: ',round(pro,1))
if apr>0:
    proap=aprobados/apr
    print('El promedio de los aprobados es: ',round(proap,1))
if rep>0:
    prore=reprobados/rep
    print('El promedio de los reprobados es: ',round(prore,1))
for i in [maxi]:
    print('La nota más alta es: ',round(i,1))
for i in [mini]:
    print('La nota más baja es:',round(i,1))