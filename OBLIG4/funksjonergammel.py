def adder(tall1, tall2):        #funksjonen som vist i oppgaven
    sum = tall1 + tall2         #enkel summasjons kode
    print("summen blir ", sum)  #og her blir svaret vist

test01=int(input("skriv tall her\n"))       #skriver første tall her
test02=int(input("skriv neste tall her\n")) #skriver andre tall her

adder(test01, test02)   #kaller prosedyren etter at verdiene har blitt definert.
                        #tall1 blir om til test01, og tall2 blir om til twst02

test03=int(input("skriv tall her\n"))       #skriver inn første tall her
test04=int(input("skriv neste tall her\n")) #skriver inn andre tall her

adder(test03, test04)   #test03 og test04 blir hva tall1 og tall2 skulle bli

def tellForekomst(minTekst, minBokstav):    #prosedyre som oppgaven beskriver
    return minTekst.count(minBokstav)       #brukte count, siden da trenger jeg bare en linje med kode for å
                                            #oppnå det oppgaven ber meg om.

tekst=input("skriv tekst her")      #skriver in teksten her
bokstav=input("skriv bokstav her")  #skriver inn bokstaven som skal bli lett etter

antall_bokstaver=tellForekomst(tekst, bokstav)   #koden blir kallt, og tekst erstatter minTekst og bokstav erstatter minBokstav

print(antall_bokstaver)
#kilde https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string
