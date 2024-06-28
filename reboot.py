#!/usr/bin/env python
import os
import time
from datetime import datatime

def schedule_reboot():
    horaReiniciar = "07:40"

    while True:
        horaAtual = datatime.now().strftime("%H: %M")

        if horaAtual == horaReiniciar:
            print(f"Hora de Reiniciar parceiro {horaReiniciar}...")
            os.system("sudo reboot") 
            break

        time.sleep(60)

if __name__ == "__main__":
    schedule_reboot()
    