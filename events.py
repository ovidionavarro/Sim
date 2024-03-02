import numpy as np
#generer variable aleatoria para el arribo de los clientes
def generawaiting_timete_poison(param):
    aux=np.random.poisson(param)
    print("1:",aux)
    while (aux==0):
        aux=np.random.poisson(param)
    print("2:",aux)
    return


    



def events(servers,time_sim,umbral):
    #servers =>numero de servidores
    #time_sim=>tiempo total de la sim
    #umbral=>valor probabilistico para determinar saltos

    #defininedo variables iniciales 
    arrival=[]#dicionario con arribo de los clientes por server 
    waiting_time=[]#tiempo de espera de cada servidor con cliente actual 
    servers_queue=[]# cantidad de clientes en cola de servidores

    time=extra_time=arrival_num=0
    arrival_time=0  
    for i in range(servers):
        arrival.append({})
        waiting_time.append(100000)
        servers_queue.append(0)
    
    while(True):
        t_at= np.random.exponential()
        arrival_time=time +t_at
        min_wait=min(waiting_time)
        
        

        #arrival_event
        if(arrival_time<min_wait and arrival_time<time_sim):
            time=arrival_time
            arrival_num+=1
            arrival[0][arrival_num]=time
            servers_queue[0]+=1
            if(servers_queue[0]==1):
                t_dt=np.random.exponential()
                waiting_time[0]=time+t_dt
        
        #exit_event
        if(min_wait<arrival_time and min_wait<time_sim):
            time=min_wait
            index_min=waiting_time.index(min_wait)#server con menor wait_time
            servers_queue[index_min]-=1 #eliminar 1 de la cola

            #verificar cantidad de clientes en cola
            if (servers_queue[index_min]==0):
                waiting_time[index_min]=100000
            else:
                t_dt=np.random.exponential()
                waiting_time[index_min]=time+t_dt

            #verificar si es el ultimo server
            if(index_min==servers-1): 
                continue

            #agregar a la cola de index_min+1 y su arrive_time 
            servers_queue[index_min +1]+=1
            arrival[index_min+1][arrival_num-sum(servers_queue[:index_min +1])]=time
            #asignar wait_time en caso de que sea 1
            if(servers_queue[index_min +1]==1):
                t_dt=np.random.exponential()
                waiting_time[index_min+1]=time+t_dt
        if(arrival_time>time_sim):
           break
    return arrival    

        
arrival=events(2,6,9)
print("arrival")
print(arrival[0])
print(arrival[1])



    

    