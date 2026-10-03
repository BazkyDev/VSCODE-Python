import threading

# Llista global per guardar les referències als temporitzadors
temporitzadors = []
segons = 0

def alarma():
    print("[ALERTA] El temporitzador X ha finalitzat!")


def cmd_set(segons):
    fil = threading.Timer(int (segons),alarma)
    temporitzadors.append(fil)
    fil.start()


def cmd_clear_all():
    for n in (temporitzadors):
        if(n.is_alive()):
            print("lalala")
    


def main():
    print("=== CONTROL DE TEMPORITZADORS ===")
    print("Opcions disponibles: SET, CLEAR, STATUS, EXIT\n")

    while True:
      
        opcio = input("Quina acció vols fer? (SET/CLEAR/STATUS/EXIT): ")
        
        if opcio == "SET":
            segons = input("Quants segons vols programar?: ")    
            cmd_set(segons)           
                
        elif opcio == "CLEAR":
            cmd_clear_all()
            
        elif opcio == "STATUS":
            cmd_status()
            
        elif opcio == "EXIT":
            cmd_clear_all()
            print("Sortint del programa...")
            break            
        else:
            print("Opció no vàlida. Introdueix SET, CLEAR, STATUS o EXIT.")

if __name__ == "__main__":
    main()
