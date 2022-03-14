def adder(tall1, tall2):        #funksjonen som vist i oppgaven
    return tall1 + tall2         #enkel summasjons kode

sum1=adder(11,12)   #sjekker summen av 2 tall
sum2=adder(32,44)   #sjekker summen av 2 tall

print("summen av 11 og 12 er ", sum1, " og summen av 32 og 44 er ", sum2)

def tellForekomst(minTekst, minBokstav):    #prosedyre som oppgaven beskriver
    return minTekst.count(minBokstav)       #brukte count, siden da trenger jeg bare en linje med kode for å
                                            #oppnå det oppgaven ber meg om.

tekst=input("skriv tekst her\n")      #skriver in teksten her
bokstav=input("skriv bokstav her for å finne ut hvor fote bokstaven blir brukt i teksten du skrev \n")  #skriver inn bokstaven som skal bli lett etter

antall_bokstaver=tellForekomst(tekst, bokstav)   #koden blir kallt, og tekst erstatter minTekst og bokstav erstatter minBokstav

print(antall_bokstaver) #teksten blir returnert
