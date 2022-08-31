import pandas as pd
import numpy as np
import math
from datetime import datetime
from datetime import time
import matplotlib.pyplot as plt
from scipy.stats.distributions import chi2

lista= pd.read_excel('/content/Taller 2.xlsx')
lista= lista.to_numpy()
datos=[]
for i in range(len(lista)):
  datos.append(lista[i][0])

def sumas(lista):
  sum=0
  for i in lista:
    sum+= i
  return sum

#Calculamos la cantidad de eventos que ocurren en cada intervalos de tiempo
#Cada intervalos de tiempo está dividido por cada hora
intervalos = [[] for i in range(24)]
suma= [i for i in range(len(datos))]
for i in range(1,24):
  for j in range(len(datos)):
    if datos[j] < time(hour=i):
      intervalos[i].append(1)

N_i = []
for i in range(len(intervalos)-1):
  N_i.append((len(intervalos[i+1])-len(intervalos[i])))
N_i.append(len(datos)-sumas(N_i))
print("Numero de eventos por cada intervalo")
print(N_i)

#Cálculo del lambda
landa= sumas(N_i)/len(N_i)
print('Lambda:', landa)

a= [i for i in range(2,10)]
n_i= []
for i in range(len(a)):
  sum=0
  for j in range(len(N_i)):
    if a[i]== N_i[j]:
      sum+=1
  n_i.append(sum)
ax=[]
for i in range(len(n_i)):
  c= ((landa)**(a[i])*math.e**(-(landa))*24)/math.factorial(a[i])
  ax.append(c)

chi=0
for i in range(len(n_i)):
  chi+= (n_i[i]-ax[i])**2/ax[i]
nivel_confianza= 0.05
grados_de_libertad= len(n_i)-1
prueba_chi= chi2.ppf(1-nivel_confianza, grados_de_libertad)
valor_p= 0.58732


print('estadisco de prueba:', chi)
print('PRUEBA.CHI.INV:', prueba_chi)

if chi<prueba_chi:
  print("No hay evidencia suficiete para rechazar la hipotesis nula, es decir la datos distribuyen Poisson")
  print('Con un valor p de', valor_p)
else:
  print("Se rechaza la hipotesis nula")
  print('Con un valor p de', valor_p)
