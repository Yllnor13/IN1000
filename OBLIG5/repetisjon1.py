mineOrd = []    #lager en tom liste

def slaaSammen(t1, t2): #definerer en ny funksjon som heter slaaSammen, med t1 og t2 som parameter
    return t1 + t2  #returnerer hva resultatet av t1 addert med t2 blir

def skrivUt(liste): #lager en ny funksjon som heter skrivUt, med "liste" som parameter
    for x in liste: #kjører koden under for hver verdi inni lista
        print(x)    #printer ut hva x blir

brukerinput = ""    #definerer verdien her før jeg skriver den inn i while koden

while brukerinput != "s":   #så lenge verdien av brukerinput ikke er lik stringen "s", så vil koden under kjøre
    brukerinput=input("skriv s om du vil avslutte koden, i om du vil legge til 2 ord som skal slås sammen, og u for å vise lista\n")
    #over er en input kode hvor brukeren skal skrive inn et bokstav.
    if brukerinput == "i":  #sjekker om brukeren skrev "i"
        text1 = input("skriv inn tekst her\n")  #brukeren skal skrive inn tekst her
        text2 = input("skriv inn tekst her\n")  #brukeren skal skrive inn tekst her
        sammen = slaaSammen(text1, text2)   #kaller koden som adderer stringene med hverandre (slaar dem sammen)
        mineOrd.append(sammen)  #legger til hva det resultatet av funksjonen blir til lista
        brukerinput= input("skriv u for å vise ordene du har lagt til eller i for å slå sammen 2 ord til\n")    #lar brukeren utføre annen kode eller avslutte
    if brukerinput == "u":  #sjekker om brukeren skrev "u"
        skrivUt(mineOrd)    #kaller funksjonen "skrivUt" med lista "mineOrd" som parameter
        brukerinput = input("lista er over, skriv i for å legge til mer eller s for å avslutte\n")  #lar brukeren kjøre koden på nytt, kjøre annen kode eller avslutte
