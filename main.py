"""
    PROGRAMMA REALIZZATO DA: PAOLO BROGI | ROSELLI SAMUELE | MOLINO ANTONIO
    
    Il programma riuscirà a eseguire l'integrazione numerica di funzioni definite su un intervallo specificato
    tramite l'utilizzo di 3 metodi:

    - RETTANGOLI
    - TRAPEZI
    - PARABOLE 

    LIBRERIE: 'numpy'

"""

import numpy as np 
import math

"""
----------------------------------------------------------------
                            FUNZIONI
----------------------------------------------------------------
"""

def F(x, funzioneInserita):
    """Restituisce una funzione scritta in notazione numpy
    Argomenti in Input:
        x: variabile in cui calcolare la funzione
        funzioneInserita (stringa): inserimento testuale dell'utente, la funzione in x.
    Argomento in Output:
        function: funzione sulla quale calcolare l'integrale.
    """

    return eval("lambda x:" + funzioneInserita)

def metodoRettangoli(f, a, b, n):
    """
    Legenda:
        f: la funzione su cui calcolare l'integrale
        a: estremo inferiore
        b: estremo superiore
        n: numero di intervalli
    Argomento in uscita:
        str: la stringa "errore" (in caso di errore di sintassi)
        float: il risultato dell'integrazione numerica
    """
    somma = 0
    for i in np.arange(a, b, (b-a)/n):
        try:
            somma += f(i)
        except Error as errore:
            return "errore"

    somma += f(b)
    somma *= (b-a)/n
    return np.around(somma, 5)

def metodoTrapezi(f, a, b, n):
    """
    Legenda:
        f: la funzione su cui calcolare l'integrale
        a: estremo inferiore
        b: estremo superiore
        n: numero di intervalli
    return:
        str: la stringa "errore", quando qualcosa è andato storto
        float: il risultato dell'integrazione numerica
    """
    somma = 0
    for i in np.arange(a, b, (b-a)/n):
        try:
            somma += 2*f(i)
        except:
            return "errore"
    somma += f(b)
    somma -= f(a) 
    somma *= (b-a)/(2*n)
    return np.around(somma, 5)

def metodoParabole(f, a, b, n):
    """
    Legenda:
        f: la funzione su cui calcolare l'integrale
        a: estremo inferiore
        b: estremo superiore
        n: numero di intervalli
    Return:
        str: la stringa "errore", quando qualcosa è andato storto
        float: il risultato dell'integrazione numerica
    """
    somma = 0
    contatore = 0
    for i in np.arange(a, b, (b-a)/n):
        try:
            if contatore % 2 == 0:
                somma += 2*f(i)
            else:
                somma += 4*f(i)
            contatore += 1
        except:
            return "error"
    somma += f(b)
    somma -= f(a) 
    somma *= (b-a)/(3*n)
    return np.around(somma, 5)

"""
----------------------------------------------------------------
                            MAIN
----------------------------------------------------------------
"""


#MAIN
#output delle istruzioni
print("""Benvenuti nel programma scritto da Molino , Brogi , Roselli \n\nBenvenuto in questo calcolatore!
Offre i tre principali metodi di integrazione numerica su un intervallo scelto.
\nISTRUZIONI:
- Inserire una funzione in x
- Usare la notazione delle funzioni e delle costanti di numpy, con il prefisso 'np.' Esempi:
    + Per il valore di pi greco, scrivere 'np.pi'
    + Per il seno di x, scrivere 'np.sin(x)'
    + Per la potenza n-esima di x, scrivere 'np.pow(x, n)
    + Per la radice quadrata, scrivere 'np.sqrt(x)'
- Rispettare le parentesi!
- Inserire numeri come estremi di integrazione.
""")
x = 0
funzioneInserita = input("Inserisci una funzione in x : ")
f = F(x, funzioneInserita)
a = float(eval(input("Inserisci l'estremo inferiore (a): ")))
b = float(eval(input("Inserisci l'estremo superiore (b): ")))
n = np.round((b-a)*10)
if not n % 2 == 0: #n deve essere pari
    n += 1
if b <= a:
    print("Gli estremi sono stati inseriti nell'ordine sbagliato. Li scambio.")
    a, b = b, a #Scambia le variabili
print("Calcolo l'integrle definito di", funzioneInserita, "tra", a, "e", b, "dividendo in", n, "intervalli.")

print("Metodo dei rettangoli. ",end = " ")
rettangoli = metodoRettangoli(f, a, b, n)
if rettangoli == "errore":
    print("\nErrore nel calcolo! Forse la funzione non è continua nell'intervallo, controlla bene.")
else:
    print("Risultato:", rettangoli)

print("Metodo dei trapezi. ",end = " ")
trapezi = metodoTrapezi(f, a, b, n)
if trapezi == "errore":
    print("\nErrore nel calcolo! Forse la funzione non è continua nell'intervallo, controlla bene.")
else:
    print("Risultato:", trapezi)

print("Metodo delle parabole. ",end = " ")
parabole = metodoParabole(f, a, b, n)
if parabole == "errore":
    print("\nErrore nel calcolo! Forse la funzione non è continua nell'intervallo, controlla bene.")
else:
    print("Risultato:", parabole)

terminatore = input("\n\nPremi un tasto per terminare.")