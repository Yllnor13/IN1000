"""
oppgave:
lag et program som åpner en tekst fil med klokkeslett i 24 format. (tiden kan være formiddag og ettermiddag)
sett innholdet inn i en liste
gjør det leselig for amerikanere gjennom en funksjon.
"""

klokketall = open("egenoppgave.txt", "r")   #lager en variabel som leser hva som er inni txt filen

klokkeslett = []    #lager en tom liste som jeg kommer til å bruke senere

for klokketid in klokketall:    #lager en for løkke som ser etter hver klokketid i klokketall
    klokkeslett.append(int(klokketid))  #legger til verdien fra hver linje som egen index på lista

print("klokkeslettene er som følgende ", klokkeslett)   #printer ut listen som blir laget over

def amerikaniser(klokker):  #lager en prosedyre som heter amerikaniser med klokker som parameter
    for x in range(len(klokker)):   #lager en for løkke for x i rekkevidden til lengden av parameteret
        if klokker[x] > 12: #sjekker om verdien er større enn 12
            klokker[x] = str(klokker[x]/2) + " pm"  #om verdien er større enn 12, så blir den delt i 2, gjort om til string og får "pm" satt til slutt
        else:   #alle andre verdier skal kjøre denne koden
            klokker[x] = str(klokker[x]) + " am"    #her blir verdien gjort om til string, og slått sammen med " am"
    return("klokkeslettene som hvordan en amerikaner vil se dem ", klokkeslett) #returnerer den nye listen

print(amerikaniser(klokkeslett))    #printer ut returnverdien til funksjonen med klokkeslett som parameter
