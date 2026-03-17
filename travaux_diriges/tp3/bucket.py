import numpy as np
from mpi4py import MPI


#Initialisation
globCom = MPI.COMM_WORLD
rank = globCom.rank
nbp = globCom.size

#Le processus 0 génère un tableau de nombres arbitraires

n = 200 #taille du tableau

if rank == 0 :
    globalData = np.random.randint(0, 800, size=n)


#Il les dispatch aux autres process

scatteredData = np.empty(n//nbp, dtype=np.int)
globCom.Scatter([globalData,MPI.INT], [scatteredData,], root=0)

#Tous les process participent au tri en parallèle

scatteredData.sort()



