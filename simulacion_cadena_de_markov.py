#importar librerías
'''
Importamos las librerías necesarias para hacer la simulación 
'''
import numpy as np
import pandas as pd
import random as rd

#creamos metodo que simula las transiciones en nuestra cedena de markov
'''
Parámetros de la función: n, siendo n el tamaño de la cadena
'''
def markov_c(n):
  '''
  Creamos la matriz de transición
  '''
  P= np.zeros((n,n)) 
  '''
  Llenamos la matriz de transición según las probabilidades dadas
  '''
  for i in range(P.shape[0]):
    for j in range(P.shape[1]):
      if i==j-1:
        P[i,j]=1/2
      if i==j+1:
        P[i,j]=1/2
  P[0,n-1]=1/2
  P[n-1,0]=1/2

  '''
  creamos un vector de booleanes que nos dice True si el estado i ya fue visitado
  '''
  estados= []
  for i in range(n): 
    estados.append(False)

  '''
  definimos el estado de partida
  '''
  estado_i= rd.randint(0,n-1)
  estado_ii= estado_i
  a= np.zeros(n)

  estados[estado_i]= True

  for i in range(len(a)):
    a[i]= i
  
  cont=0
  '''
  Aqui hacemos las transiciones y calculamos la cantidad de pasos que tarda
  en visitar los n estados
  '''
  while not all(estados):
    estado_ii= int(np.random.choice(a,p=P[estado_ii]))
    estados[estado_ii] = True
    cont+=1

  return cont

#Simulación
'''
empezamos la simulación: son 1000 iteraciones por cada tamaño de la cadena
'''
def simulacion(tamCadena,nSim):
  t_cub= []
  for i in range(3,tamCadena):
    #print(i)
    sum = 0
    for j in range(nSim):
      sum = sum + markov_c(i)
    t_cub.append([i,i*(i-1)/2,sum/nSim, abs(i*(i-1)/2-sum/nSim)])

  '''
  imprimimos los resultados
  '''
  t_cub= pd.DataFrame(t_cub).set_axis(['n','t_cub teorico','t_cub simulado', 'error'],axis=1)
  return t_cub

tamaños_cadena=15
numero_simulaciones= 1000
simulacion(tamaños_cadena,numero_simulaciones)
