# Contrução de um cronomentro
import os   # Importe de biblioteca que integra com o sistema operacional
import time # Importe utilizado para usar tempo no Python

segundo  = 0
minuto = 0


while True:
    os.system('cls')
    if segundo == 60:
        segundo = 0
        minuto += 1
    if segundo < 10:
        print(f"0{minuto}:0{segundo}")
    else:
        print(f"0{minuto}:{segundo}")
    time.sleep(1)
    segundo += 1
