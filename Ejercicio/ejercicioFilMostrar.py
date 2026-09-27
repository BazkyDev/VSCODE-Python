import threading

def mostrarllista():
    for i in range(10):
        print(i)


hilo = threading.Thread ( target=mostrarllista)
hilo.start()
hilo.join
print('final')

    