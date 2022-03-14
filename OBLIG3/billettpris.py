#oppgave 3

#oppgave 3.1
def billettkjoep():
    alder=int(input("skriv alderen din her.\n"))
    #oppgave 3.2
    billettpris=0
    #oppgave 3.3
    if alder <= 17:#Sjekker alltid om noe er mindre enn alder, fordi om den så etter alle som var eldre enn 17 som voksne, så hadde ikke if testen gått videre enn den første elifen. og da får ikke 63 åringer sin pris.
        billettpris+=30
    elif alder <63:#om de er mellom 18 og 62, så blir prisen voksen pris
        billettpris+=50
    else:
        billettpris+=35
    #oppgave 3.4
    print("da er prisen din ", billettpris)
#oppgave 3.5
billettkjoep()
billettkjoep()
billettkjoep()
billettkjoep()

#oppgave 3.6
"""
brukeren kan skrive bokstaver, som ikke hadde funket med koden. da får man en traceback error, siden alder aksepterer bare heltall (int)
ellers så kunne de ha skrevet aldre som er umulig å oppnå (for eksempel alder på over 200). Hadde ikke skjedd noe dårlig, prisen ville ha vært det samme som alle andre som er eldre enn 63
det kan også hende at de skriver float tall, som vil føre til enda en traceback error.
"""
