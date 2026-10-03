import threading


def alarma():
    print("Alarma")


fil = threading.Timer(5, alarma)
fil.start()