skrivtall = -1  #har bare en verdi som ikke er null
talliste=[] #starter lista her
while skrivtall != 0:   #while løkke slik at koden under blir brukt igjen helt til brukeren skriver 0
    skrivtall=int(input("skriv tall her\n"))    #bruker int for
    talliste.append(skrivtall)#bruker append for å legge til noe til slutt her

tall=0
minSum=0

for talliliste in talliste:#for løkke som sjekker tall i listen, og printer ut summen av talla
    print (talliste[tall])
    minSum+=talliste[tall]#adderer verdien av en liste entry
    tall += 1#får den til å gå til neste tall

print("summen av alle talla i lista blir ", minSum)#bare tekst som sier hva summen er

minst=talliste[0]

for minstetall in talliste:#løkke som skal sjekke gjennom entryene i lista
    if minstetall < minst: #sjekker om verdien til minstetall er mindre enn minst
        minst=minstetall#gjør det minste tallet som blir funnet om til det minste tallet

print(minst)#printer ut det minste tallet

stoerst=talliste[0]

for stoerstetall in talliste:#samme ide her som over, bare motsatt
    if stoerstetall > stoerst:#sjekker etter om tallet den fant er større enn de før
        stoerst=stoerstetall #erstatter den forrige verdien med det største tallet den finner

print(stoerst)#printer ut det største tallet
