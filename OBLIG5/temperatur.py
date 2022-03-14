temptext = open("temperatur.txt", "r")  #lager en variabel som åpner og leser hva som er inni temperatur.txt

templiste = []  #lager en tom liste med navn "templiste"

for linje in temptext:  #for hver linje i temptext så kjører koden under
    templiste.append(int(linje))    #legger til int av hva som er inni txt filen inni lista

temptext.close()    #lukker lista

print(templiste)    #printer listen

def gjennomsnittavtemp(temperaturliste):    #definerer ny funksjon med parameter "temperaturliste"
    sumtemperatur = 0   #summen av temperaturen er lik 0 (ville bare definere variabelen)
    for temp in range(len(temperaturliste)):    #for hver verdi innenfor størrelsen av lista, så skal koden under kjøre
        sumtemperatur += temperaturliste[temp]  #variabel sumtemperatur blir addert med verdier fra lista
    return sumtemperatur/len(temperaturliste)   #variabel sumtemperatur blir dividert med mengen av indexer på lista

print(gjennomsnittavtemp(templiste))    #kaller koden gjennom print, og bruker templista som parameter
