import random
import math
import time

DADI = [4, 6, 8, 10, 12, 20, 100]

def tira_dadi(tipo_dado, quanti_lanci):
    random.seed(math.floor(time.time()))
    risultatiLanci = []
    for _ in range(quanti_lanci):
        risultato = random.randint(1, tipo_dado)
        risultatiLanci.append(risultato)
    return risultatiLanci