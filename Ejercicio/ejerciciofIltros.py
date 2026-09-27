import threading

def contar(*args):
    contador=args[0] #0 
    inctrmento = args[1] #1
    limite=args[2]          #10
    num_hilo=args[3]        #num_hilo
    while contador<=limite:
        print('HILO: ', num_hilo, 'contador:', contador)
        contador+=inctrmento


for num_hilo in range(3):
    #les funcions de fil han de rebre el arguments amb arg*
    hilo = threading.Thread ( target=contar, args=( 0,1,10, num_hilo))
    hilo.start()
        