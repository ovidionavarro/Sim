import numpy as np
#generer variable aleatoria para el arribo de los clientes
def generate_poison(param):
    aux=np.random.poisson(param)
    print("1:",aux)
    while (aux==0):
        aux=np.random.poisson(param)
    print("2:",aux)
    return
print( generate_poison(2))

    



def events(servers,time_sim,umbral):
    #servers =>numero de servidores
    #time_sim=>tiempo total de la sim
    #umbral=>valor probabilistico para determinar saltos

    #defininedo variables iniciales 
    arrival=[]#dicionario con arribo de los clientes por server 
    waiting_time=[]#tiempo de espera de cada servidor con cliente actual 
    servers_queue=[]# cantidad de clientes en cola de servidores

    time=extra_time=arrival_num=arrival_time=0
    t_at=generate_poison(2)   
    for i in range(servers):

        waiting_time.append(10000)
        servers_queue.append(0)
    
    while(True):
        arrival_time=time+t_at
        t_at=0
        min_wait=min(waiting_time)

        if(arrival_time<min_wait and arrival_time<time_sim):
            time=arrival_time
            num_arrival+=1
            servers_queue[0]+=1
            if(len(servers_queue[0])==1):
                t_dt=np.random.exponential()
                waiting_time[0]=time+t_dt


        



    

    