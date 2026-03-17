from mpi4py import MPI
from math import log2


globCom = MPI.COMM_WORLD.Dup()
rank = globCom.rank
nbp  = globCom.size

dim = int(log2(nbp))
assert(2**dim == nbp), "Le nb de processus doit être une puissance de 2"

jeton = None
if rank == 0:
    print(f"Dimensin du cube : {dim}")
    jeton = 67


for d in range(dim): 
    if rank < 2**d: #chaque processus détenteur distribue le jeton
        dest = rank + 2**d
        print(f"Processus {rank} envoie le jeton {jeton} au processus {dest}", flush=True)
        globCom.send(jeton, dest=dest, tag = d)
    elif rank < 2**(d+1): #réception du jeton
        src = rank - 2**d
        jeton = globCom.recv(source=src, tag=d)
        print(f"Processus {rank} reçoit le jeton {jeton} du processus {src}", flush=True)
