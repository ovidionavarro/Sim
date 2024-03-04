import numpy as np
from queue import Queue
#generer variable aleatoria para el arribo de los clientes
def generawaiting_timete_poison(param):
    aux=np.random.poisson(param)
    print("1:",aux)
    while (aux==0):
        aux=np.random.poisson(param)
    print("2:",aux)
    return

def encontrar_llave(list,int, valor):
    dic=list[int]
    for key, val in dic.items():
        if val == valor:
            return key
    return 'error de valor'
    



def events(servers,time_sim,umbral):
    #servers =>numero de servidores
    #time_sim=>tiempo total de la sim
    #umbral=>valor probabilistico para determinar saltos

    #defininedo variables iniciales 
    arrival=[]#diccionario con arribo de los clientes por server 
    waiting_time=[]#tiempo de espera de cada servidor con cliente actual 
    client_queue=[]#clientes en cola de cada servidor

    client_out=time=extra_time=arrival_num=0
    arrival_time=0  
    for i in range(servers):
        arrival.append({})
        client_queue.append(Queue())
        waiting_time.append(100000)
    
    while(True):
        t_at= np.random.exponential()
        arrival_time=time +t_at
        min_wait=min(waiting_time)
        
        

        #arrival_event
        if(arrival_time<min_wait and arrival_time<time_sim):
            time=arrival_time
            arrival_num+=1
            arrival[0][arrival_num]=time
            client_queue[0].put(arrival_num)#agregar clientes a cola del servidor 0
            if(client_queue[0].qsize()==1):
                t_dt=np.random.exponential()
                waiting_time[0]=time+t_dt
        
        #exit_event
        if(min_wait<arrival_time and min_wait<time_sim):
            time=min_wait
            index_min=waiting_time.index(min_wait)#server con menor wait_time
            client=client_queue[index_min].get()#quitar elemento de la cola

            #verificar cantidad de clientes en cola
            if (client_queue[index_min].empty()):
                waiting_time[index_min]=100000
            else:
                t_dt=np.random.exponential()
                waiting_time[index_min]=time+t_dt

            #verificar si es el ultimo server
            if(index_min==servers-1): 
                client_out+=1
                continue
 
            client_queue[index_min+1].put(client) #agregar a la cola de index_min+1 y su arrive_time 
            arrival[index_min+1][client]=time
            
            if(client_queue[index_min +1].qsize()==1):#asignar wait_time en caso de cola 1
                t_dt=np.random.exponential()
                waiting_time[index_min+1]=time+t_dt
        
        
        if(arrival_num-client_out!=0 and min(min_wait,arrival_time)>time_sim ):
            time=min_wait
            index_min=waiting_time.index(min_wait)
            client=client_queue[index_min].get(arrival_num)#agregar clientes a cola del servidor 0
            
            #verificar cantidad de clientes en cola
            if(client_queue[index_min].empty()):
                waiting_time[index_min]=100000
            else:
                t_dt=np.random.exponential()
                waiting_time[index_min]=time+t_dt
            
            #verificar si es el ultimo server
            if(index_min==servers-1):
                client_out+=1
                continue

            client_queue[index_min+1].put(client)#agregar a la cola de index_min+1 y su arrive_time
            arrival[index_min+1][client]=time
            
            if(client_queue[index_min +1].qsize()==1):#asignar wait_time en caso de cola=1
                t_dt=np.random.exponential()
                waiting_time[index_min+1]=time+t_dt
        #caso donde se pase del tiempo y no existan client en el sistema
        if(arrival_num-client_out==0 and min(min_wait,arrival_time)>time_sim ):
            break
        
    return arrival,client_out,client_queue  

        
arrival,client_out,client_queue=events(3,6,9)
#a=client_queue[0]
#while not a.empty():
#    elemento = a.get()
#    print(elemento)
#print(exit_time)
print("arrival")
print(arrival[0])
print(arrival[1])
print(arrival[2])



#mi_cola = Queue()
#mi_cola.put(1)
#mi_cola.put(2)
#mi_cola.put(3)
#
#print(mi_cola.qsize())
#
#
## Obtener y mostrar los elementos de la cola
#
#elemento = mi_cola.get()
#print(elemento)
#elemento2= mi_cola.get()
#print(elemento2)
#












    



    

    