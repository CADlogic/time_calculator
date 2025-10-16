from datetime import datetime

# Chiede all'utente di inserire la data di nascita
data_nascita_str = input("Inserisci la tua data di nascita (giorno/mese/anno): ")

# Converte la stringa in un oggetto datetime
try:
    data_nascita = datetime.strptime(data_nascita_str, "%d/%m/%Y")
except ValueError:
    print("Formato della data non corretto. Usa il formato giorno/mese/anno.")
    exit()

# Ottiene la data corrente
oggi = datetime.now()

# Calcola la differenza in anni, mesi e giorni
anni = oggi.year - data_nascita.year
mesi = oggi.month - data_nascita.month
giorni = oggi.day - data_nascita.day

# Se i giorni sono negativi, significa che l'anno corrente non ha ancora raggiunto il mese di nascita
if giorni < 0:
    mesi -= 1
    giorni += 30  # Questa è una semplificazione, poiché i mesi non hanno tutti 30 giorni

# Se i mesi sono negativi, significa che l'anno corrente non ha ancora raggiunto il mese di nascita
if mesi < 0:
    anni -= 1
    mesi += 12

# Stampa il risultato
print(f"Hai {anni} anni, {mesi} mesi e {giorni} giorni.")