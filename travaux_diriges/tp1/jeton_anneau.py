from mpi4py import MPI

globCom = MPI.COMM_WORLD.Dup()
rank = globCom.rank
nbp  = globCom.size

jeton = None
if rank==0: 
    jeton = 1
    globCom.send(jeton,dest=1,tag=67)  #on envoie jeton au processus 1
    jeton = globCom.recv(source=nbp-1,tag=67) # on met dans jeton ce que le dernier processus nous envoie (= rien si c'est le premeir passage)
    print(f"jeton reçu : {jeton}") #on affiche
else:
    jeton = globCom.recv(source=rank-1,tag=67)
    jeton += 1
    globCom.send(jeton,dest=(rank+1)%nbp, tag=67) #on l'envoie au suivant, modulo nbp (ce qui permet de boucler sur 0)
