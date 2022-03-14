#oppgave 1

#oppgave 1.1

tall = [3, 2, 8]

tall.append(6) #var ikke sikker på hvordan jeg skulle tolke oppgaven, så jeg la til append her istedenfor å legge til et ekstra tall på lista manuelt.


print(tall[0], tall[2])


#oppgave 1.2

maxnavn=4

listemednavn = []

while len(listemednavn) < maxnavn: #her så kjører koden så lenge lendgen av listemednavn er mindre enn maxnavn, som gir brukeren evnen til å skrive bare 4 navn
    elever = input("skriv navn her, husk på stor forbokstav!\n") #ber brukeren bruke stor forbokstav slik at de ikke får galt svar når de skriver navnet mitt
    listemednavn.append(elever)

#oppgave 1.3

navn="Yllnor" #sjekker etter navnet mitt

if navn in listemednavn:
    print("du husket meg!")
else:
    print("glemte du noen?")


#oppgave 1.4


tall_sum=sum(tall)#brukte sum koden her slik at jeg kunne få summen av alle tallene der

#print(tall_sum)#vet at oppgaven ikke ber om å printe ut tallene, men jeg gjorde dette slik at jeg kunne verifisere at det ble summen

tall_produkt= tall[0]*tall[1]*tall[2]*tall[3]

#print(tall_produkt)#vet at oppgaven ikke ber om å printe ut tallene, men jeg gjorde dette slik at jeg kunne verifisere at det ble produktet

tall_multi_sum=[tall[0]*tall[1]*tall[2]*tall[3], sum(tall)]

#print(tall_multi_sum)vet at oppgaven ikke ber om å printe ut tallene, men jeg gjorde dette slik at jeg kunne verifisere at det ble en liste med sum og produkt

#tall.append(tall_multi_sum)#kan bruke denne koden her, men da syntes jeg at det så rart ut med hvordan printen ble

#tall=[tall, tall_multi_sum]#listene er slått sammen

tall.extend(tall_multi_sum)

print(tall)

tall.pop(4)

tall.pop(4)#skrev tall pop 2 ganger, slik at den først fjernet det 5 tallet (nest siste tallet), og så igjen(slik at det siste tallet blir fjernet)

print(tall)

#en ting jeg ikke var sikker på var hva oppgaven mente med å slå sammen listene. Jeg valgte å ha det slik at tall_multi_sum blir

#hjelp fra denne siden https://stackoverflow.com/questions/21043387/how-do-you-add-input-from-user-into-list-in-python
#hjelp fra denne siden http://www.datamaskin.biz/Programmering/python-programming/94027.html
