import random
import pandas as pd
import numpy as np

def simulacion(n,a):
  p_votos= [i for i in range(1,n+1) ]
  votes_a = random.sample(p_votos,a)
  zeta= [2 for i in range(n)]
  for i in votes_a:
    zeta[i-1]=0
  s= np.cumsum(zeta)
  G=[]
  for i in range(len(s)): 
    if s[i] < p_votos[i]:
      G.append(1)
    else:
      G.append(0)
  if 0 in G:
    return 0
  else:
    return 1
def elecciones(n,nSim):
  win_A= [i for i in range(int(n/2)+1,n+1)]
  p_simulacion= np.zeros(len(win_A))
  for i in range(len(win_A)):
    for j in range(nSim):
      p_simulacion[i] += simulacion(n,win_A[i]) 
    p_simulacion[i] /= nSim
  
  teorico= [(win_A[i]-(n-win_A[i]))/n for i in range(len(win_A))]

  resultados= []
  for i in range(len(win_A)):
    resultados.append([win_A[i],p_simulacion[i],teorico[i]])
  resultados.append(['n='+str(n),'nSim=' +str(nSim)])

  resultados= pd.DataFrame(resultados).set_axis(['A','Prob. Simulación', 'Prob. Teórica'],axis=1)
  return resultados

elecciones(20,10000)
